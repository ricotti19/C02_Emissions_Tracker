from flask import Flask, render_template, request, redirect
import sqlite3


app = Flask(__name__)
DB = "co2data.db"


# Load with 20 major Texas cities
def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT UNIQUE,
            emission_kg REAL
        )
    """)
    c.execute("SELECT COUNT(*) FROM cities")
    if c.fetchone()[0] == 0:
        sample_cities = [
            ("Austin", 0),
            ("Dallas", 0),
            ("Houston", 0),
            ("San Antonio", 0),
            ("El Paso", 0),
            ("Fort Worth", 0),
            ("Arlington", 0),
            ("Corpus Christi", 0),
            ("Plano", 0),
            ("Laredo", 0),
            ("Garland", 0),
            ("Irving", 0),
            ("Amarillo", 0),
            ("Grand Prairie", 0),
            ("McKinney", 0),
            ("Frisco", 0),
            ("Brownsville", 0),
            ("Pasadena", 0),
            ("Mesquite", 0),
            ("Killeen", 0)
        ]
        c.executemany("INSERT INTO cities (city, emission_kg) VALUES (?,?)", sample_cities)
    conn.commit()
    conn.close()


init_db()


# Distance and vehicle type to calculate emissions
def calculate_emission(distance, vehicle):
    factors = {"Gasoline":0.25, "Diesel":0.22, "Hybrid":0.10, "Electric":0.0}
    return distance * factors.get(vehicle, 0.25)


# Update city emissions and insert city if not present
def update_city_emission(city, distance, vehicle):
    emission = calculate_emission(distance, vehicle)
    city = city.strip().title()
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("UPDATE cities SET emission_kg = emission_kg + ? WHERE city = ?", (emission, city))
    if c.rowcount == 0:
        c.execute("INSERT INTO cities (city, emission_kg) VALUES (?, ?)", (city, emission))
    conn.commit()
    conn.close()
    return emission


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Reset emissions option
        if request.form.get("reset") == "1":
            conn = sqlite3.connect(DB)
            c = conn.cursor()
            c.execute("UPDATE cities SET emission_kg = 0")
            conn.commit()
            conn.close()
            return redirect("/")
        city = request.form["city"].strip()
        distance = float(request.form["distance"])
        vehicle = request.form["vehicle"]
        if city and distance and vehicle:
            update_city_emission(city, float(distance), vehicle)
        return redirect("/")


    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT city, emission_kg FROM cities ORDER BY city ASC")
    data = c.fetchall()
    conn.close()


    labels = [row[0] for row in data] #City names
    values = [row[1] for row in data] #Emissions


    return render_template("index.html", labels=labels, values=values)


if __name__ == "__main__":
    app.run(debug=True)



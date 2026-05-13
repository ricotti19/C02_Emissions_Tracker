# Imports Flask framework tools
from flask import Flask, render_template, request, redirect
import sqlite3

# Create Flask app
app = Flask(__name__)

# Database file name
DB = "co2data.db"


# Initialize database with Texas cities
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

    # Only preload cities if table is empty
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

        c.executemany(
            "INSERT INTO cities (city, emission_kg) VALUES (?, ?)",
            sample_cities
        )

    conn.commit()
    conn.close()


# Run database setup
init_db()


# Calculate emissions based on vehicle type
def calculate_emission(distance, vehicle):

    factors = {
        "Gasoline": 0.25,
        "Diesel": 0.22,
        "Hybrid": 0.10,
        "Electric": 0.0
    }

    return distance * factors.get(vehicle, 0.25)


# Update city emission total
def update_city_emission(city, distance, vehicle):

    emission = calculate_emission(distance, vehicle)

    city = city.strip().title()

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    # Update existing city
    c.execute(
        "UPDATE cities SET emission_kg = emission_kg + ? WHERE city = ?",
        (emission, city)
    )

    # Insert city if it doesn't exist
    if c.rowcount == 0:
        c.execute(
            "INSERT INTO cities (city, emission_kg) VALUES (?, ?)",
            (city, emission)
        )

    conn.commit()
    conn.close()

    return emission

@app.route("/", methods=["GET", "POST"])
def home():
    error = None

    if request.method == "POST":
        # 1. CHECK RESET FIRST
        if request.form.get("reset") == "1":
            conn = sqlite3.connect(DB)
            c = conn.cursor()
            c.execute("UPDATE cities SET emission_kg = 0")
            conn.commit()
            conn.close()
            return redirect("/")

        # 2. ONLY ATTEMPT DATA PROCESSING IF NOT RESETTING
        # Use .get() to avoid KeyError if the form is empty
        city = request.form.get("city", "").strip()
        vehicle = request.form.get("vehicle")
        distance_raw = request.form.get("distance")

        try:
            distance = float(distance_raw)

            if distance < 0:
                error = "Distance cannot be negative."
            elif not city:
                error = "Please enter a city name."
            else:
                update_city_emission(city, distance, vehicle)
                return redirect("/")

        except (ValueError, TypeError):
            error = "Please enter a valid number."

    # Load chart data
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
        SELECT city, emission_kg
        FROM cities
        ORDER BY city ASC
    """)

    data = c.fetchall()

    conn.close()

    # Separate city names and emission values
    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template(
        "index.html",
        labels=labels,
        values=values,
        error=error
    )


# Run app
if __name__ == "__main__":
    app.run(debug=True)
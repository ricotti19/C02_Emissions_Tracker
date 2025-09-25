# C02_Emissions_Tracker
## Basic Info
**PM Info**
- Name: Shriya Shenoj
- GitHub: [@ricotti19](https://github.com/ricotti19)
- Discord: [@ss031804](https://discord.com/users/ss031804)

**Description**
CO2 Emissions Tracker web app built with Python (Flask), HTML, and SQLite. 
Users can log trips by selecting a city (from 20 Texas cities), entering the distance in kilometers, and choosing one of four vehicle types - hybrid/electric/diesel/gasoline. 
The app calculates CO2 emissions based on these inputs, stores the totals in the database, and displays an interactive bar chart to compare emissions across cities.
Demonstrates basic front-end web development and back-end database integration skills.
### Dependencies
* [Python 3.13.7](https://www.python.org/downloads/release/python-3137/) or higher
* [Flask 3.1.2](https://pypi.org/project/Flask/) — Install using `pip install flask`
* [SQLite](https://www.sqlite.org/download.html) — Usually is pre-installed as part of Python
* [Chart.js](https://www.chartjs.org/) — Included via CDN in index.html
### Installation
```bash
1. Clone the repository:
git clone https://github.com/ricotti19/CO2-Emissions-Tracker.git

2. Navigate into the folder:
cd C02_Emissions_Tracker

3. Install dependencies:
pip install Flask==3.1.2
pip install Jinja2==3.1.6
pip install click==8.3.0
pip install colorama==0.4.6
pip install blinker==1.9.0
pip install itsdangerous==2.2.0
pip install markupsafe==3.0.2
pip install werkzeug==3.1.3

Note: these packages are needed in order to run c02_emissions_tracker.py

4. Run the app:
python c02_emissions_tracker.py

5. Open the app in browser:
(Go to) http://127.0.0.1:5000 (to view the interactive app)

```

### Folder Structure
```text
DFR/
├── templates/
│   └── index.html
├── co2_emissions_tracker.py
├── co2data.db
├── trips.db
└── README.md
```

### Usage
1. Select a city from the dropdown menu listing 20 Texas cities
2. Enter the trip distance (km)
3. Choose the vehicle type (hybrid/electric/diesel/gasoline)
4. Click **Add Trip** to update the chart
5. If needed, click **Reset All Emissions** to start over

### Example of output
<img width="1908" height="996" alt="image" src="https://github.com/user-attachments/assets/fe451b84-982f-4e04-b1b7-02e3feef55d4" />


## CO2 Emissions Tracker

### Web app built with Python (Flask), HTML, and SQLite where users can log trips by selecting from 20 Texas cities, enter the distance in kilometers, and choose one of four given vehicle types to view an interactive bar chart that compares emissions across cities.

## ✨ Features
* **Modern Interface:** Responsive dashboard built with Tailwind CSS featuring a glassmorphic design.
* **Interactive Data:** Dynamic bar charts powered by Chart.js for real-time emissions comparison.
* **Data Integrity:** Server-side validation logic in `c02_emissions_tracker.py` to prevent invalid data entry (e.g., negative distances).
* **Persistent Storage:** SQLite database integration for reliable trip logging and retrieval.

## 🛠️ Tech Stack
* **Backend:** Python / Flask
* **Database:** SQLite (ACID compliant)
* **Frontend:** HTML5 / Tailwind CSS / Chart.js

## File Structure
```text
C02_Emissions_Tracker/
├── templates/
│   └── index.html
├── c02_emissions_tracker.py
├── co2data.db
├── DFR Onboarding.ipynb
├── package-lock.json
├── README.md
└── trips.db
```

## 🚀 Setup & Installation in terminal
1. **Install Flask:**
   ```bash
   pip install flask
   ```
2. **Run Application:**
   ```bash
   python c02_emissions_tracker.py
   ```
3. **Open browser and navigate to:**
   ```bash
   http://127.0.0.1:5000
   ```

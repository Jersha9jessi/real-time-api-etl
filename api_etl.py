import sqlite3
import requests
from datetime import datetime

# 1. Extract: Public API నుండి రియల్-టైమ్ డేటాని తీసుకోవడం (ఉదాహరణకు పబ్లిక్ వెదర్ డేటా)
API_URL = "https://api.open-meteo.com/v1/forecast?latitude=17.3850&longitude=78.4867&current_weather=true"

def fetch_data():
    try:
        response = requests.get(API_URL, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get('current_weather')
        else:
            print(f"API Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Connection Failed: {e}")
        return None

# 2. Transform & Load: డేటాని క్లీన్ చేసి SQLite డేటాబేస్ లో సేవ్ చేయడం
def save_to_database(weather):
    if not weather:
        print("No data to save.")
        return

    conn = sqlite3.connect('weather_pipeline.db')
    cursor = conn.cursor()

    # టేబుల్ లేకపోతే క్రియేట్ చేయడం
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL,
            windspeed REAL,
            winddirection REAL,
            timestamp TEXT
        )
    ''')

    # డేటా ఇన్‌సర్ట్ చేయడం
    temp = weather.get('temperature')
    windspeed = weather.get('windspeed')
    winddir = weather.get('winddirection')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute('''
        INSERT INTO weather_logs (temperature, windspeed, winddirection, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (temp, windspeed, winddir, timestamp))

    conn.commit()
    conn.close()
    print(f"[{timestamp}] Success: Weather Data Loaded to SQLite Database!")

if __name__ == "__main__":
    weather_data = fetch_data()
    save_to_database(weather_data)

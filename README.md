# Real-Time Weather ETL Pipeline 🌤️

An end-to-end automated ETL (Extract, Transform, Load) data engineering pipeline built entirely within a mobile Linux environment (**Termux**), extracting live meteorological data and storing it in a local relational database.

## 🚀 Project Overview
This project demonstrates how lightweight, serverless-style data pipelines can be engineered and scheduled on non-traditional infrastructure (Android/Termux). It fetches real-time weather metrics from the Open-Meteo REST API, processes the payload, and loads it into a structured SQLite database for continuous tracking.

## 🛠️ Tech Stack
- **Language:** Python 3
- **Data Source:** Open-Meteo REST API
- **Storage:** SQLite (`weather_pipeline.db`)
- **Automation & Scheduling:** Linux `cron` (`cronie`), `termux-wake-lock`
- **Version Control:** Git & GitHub

## 📂 Project Architecture
```text
[Open-Meteo API] ---> (Python ETL Script) ---> [SQLite Database]
                              ^
                       (Cron Scheduler)

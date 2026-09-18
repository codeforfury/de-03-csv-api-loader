# CSV/API to Local Database Loader

## Overview
This project builds a modular ETL (Extract, Transform, Load) pipeline that fetches public holiday data from a free API, cleans it, and loads it into a local SQLite database. It's the third project in a broader Data Engineering portfolio, introducing the core ETL pattern using separate, reusable Python modules — a structure that mirrors how real-world pipelines are organized.

## Data Source
- **API:** [Nager.Date Public Holidays API](https://date.nager.at/) — free, no API key required
- **Endpoint used:** Public holidays for the United States, 2025

## Pipeline Structure
The pipeline is split into three independent, reusable modules:

- **`step1_extract.py`** — fetches raw holiday data from the API
- **`step2_transform.py`** — cleans the data: drops a fully-empty column, fills meaningful nulls, and converts list-type fields into plain text (required for SQLite storage)
- **`step3_load.py`** — loads the cleaned data into a local SQLite database

`main.py` orchestrates all three steps in sequence, so the full pipeline can be run with a single command.

## What Was Done
- Extracted holiday data via a live API call
- Investigated and handled a fully-null column (`launchYear`) by dropping it
- Handled meaningful nulls in `counties` (null = nationwide holiday)
- Discovered and fixed a data type issue: list-type fields (`types`, `counties`) cannot be stored directly in SQLite and were converted to comma-separated text
- Loaded 17 cleaned records into a `holidays` table in `data/loader.db`

## Project Structure
```
de-03-csv-api-loader/
├── data/
│ └── loader.db # SQLite database with cleaned holiday data
├── notebooks/
│ └── exploration.ipynb # Scratch space for initial data exploration
├── src/
│ ├── step1_extract.py # Extract: fetch data from API
│ ├── step2_transform.py # Transform: clean and reshape data
│ ├── step3_load.py # Load: write data into SQLite
│ └── main.py # Orchestrates the full pipeline
├── requirements.txt
└── README.md
```

## Tech Stack
- Python
- Pandas
- Requests (for API calls)
- SQLite

## Key Takeaways
This project introduced the complete ETL pattern and modular pipeline design — splitting extract, transform, and load logic into independent, testable files rather than one large script. It also involved real-world debugging: handling an unexpectedly deprecated API, and discovering/fixing a data type incompatibility (Python lists vs. SQLite storage) through actual error messages rather than guesswork.

## How to Run
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the full pipeline: `python src/main.py`
4. Open `data/loader.db` in DB Browser for SQLite to view the loaded data
# Student Performance Dashboard

Short description: data pipeline + SQL integration + visualizations to track student academic performance.

## Setup
1. python -m venv venv
2. source venv/bin/activate   # or venv\Scripts\activate on Windows
3. pip install -r requirements.txt

## Run
- Clean data: `python scripts/clean_data.py data/sample/students_raw.csv`
- Import to SQLite: `python scripts/import_sqlite.py data/cleaned/students.csv`
- Run notebooks in `/notebooks` for visualizations.

## Contributing
See CONTRIBUTING.md

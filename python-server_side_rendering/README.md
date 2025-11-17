# Python - Server-Side Rendering

This project demonstrates server-side rendering (SSR) using Python and Flask with the Jinja templating engine.

## Project Structure

- `task_00_intro.py` - Template generation function with error handling
- `task_01_jinja.py` - Basic Flask application with Jinja templates
- `task_02_logic.py` - Dynamic templates with loops and conditions
- `task_03_files.py` - Display data from JSON and CSV files
- `task_04_db.py` - Extended to include SQLite database support
- `create_database.py` - Script to create and populate the SQLite database
- `templates/` - HTML templates directory
- `items.json` - Sample items data
- `products.json` - Sample products data in JSON format
- `products.csv` - Sample products data in CSV format
- `products.db` - SQLite database (created by running create_database.py)

## Installation

```bash
pip install Flask
```

## Usage

### Task 0: Template Generation
```python
from task_00_intro import generate_invitations

with open('template.txt', 'r') as file:
    template_content = file.read()

attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
]

generate_invitations(template_content, attendees)
```

### Task 1: Basic Flask App
```bash
python3 task_01_jinja.py
```
Visit http://localhost:5000/, http://localhost:5000/about, or http://localhost:5000/contact

### Task 2: Dynamic Templates
```bash
python3 task_02_logic.py
```
Visit http://localhost:5000/items

### Task 3: JSON/CSV Data Display
```bash
python3 task_03_files.py
```
Visit:
- http://localhost:5000/products?source=json
- http://localhost:5000/products?source=csv
- http://localhost:5000/products?source=json&id=1

### Task 4: SQLite Database
First, create the database:
```bash
python3 create_database.py
```

Then run the app:
```bash
python3 task_04_db.py
```
Visit:
- http://localhost:5000/products?source=sql
- http://localhost:5000/products?source=sql&id=2

## Learning Objectives

- Understand server-side rendering vs client-side rendering
- Implement SSR using Flask and Jinja
- Work with dynamic content from JSON, CSV, and SQLite
- Handle errors and edge cases gracefully
- Create reusable templates with includes

## Author

Holberton School Project

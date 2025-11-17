# Testing Guide

## Prerequisites

Install Flask if not already installed:
```bash
pip install Flask
```

## Task 0: Template Generation

Create a test file to use the function:

```python
from task_00_intro import generate_invitations

# Read template
with open('template.txt', 'r') as file:
    template_content = file.read()

# Define attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Generate invitations
generate_invitations(template_content, attendees)
```

Expected: Creates `output_1.txt`, `output_2.txt`, `output_3.txt` with personalized invitations.

### Test Edge Cases:

```python
# Empty template
generate_invitations("", attendees)  # Should print error message

# Empty attendees
generate_invitations(template_content, [])  # Should print error message

# Invalid types
generate_invitations(123, attendees)  # Should print error message
generate_invitations(template_content, "not a list")  # Should print error message
```

## Task 1: Basic Flask Application

Run the Flask app:
```bash
python3 task_01_jinja.py
```

Test the following URLs in your browser:
- http://localhost:5000/ (Home page)
- http://localhost:5000/about (About page)
- http://localhost:5000/contact (Contact page)

Expected: Each page displays with header (navigation) and footer.

## Task 2: Dynamic Templates

Run the Flask app:
```bash
python3 task_02_logic.py
```

Test:
- http://localhost:5000/items

Expected: Displays list of items from `items.json`

Test with empty items:
1. Edit `items.json` to have empty array: `{"items": []}`
2. Reload page
3. Expected: "No items found" message

## Task 3: JSON/CSV Files

Run the Flask app:
```bash
python3 task_03_files.py
```

Test the following URLs:
- http://localhost:5000/products?source=json (all products from JSON)
- http://localhost:5000/products?source=csv (all products from CSV)
- http://localhost:5000/products?source=json&id=1 (filter by id)
- http://localhost:5000/products?source=csv&id=2 (filter by id)
- http://localhost:5000/products?source=xml (invalid source - error)
- http://localhost:5000/products?source=json&id=999 (not found - error)

Expected:
- Valid sources display products in a table
- Invalid source shows "Wrong source"
- Invalid id shows "Product not found"

## Task 4: SQLite Database

First, create the database:
```bash
python3 create_database.py
```

Expected output: "Database created and populated successfully!"

Run the Flask app:
```bash
python3 task_04_db.py
```

Test the following URLs:
- http://localhost:5000/products?source=sql (all products from database)
- http://localhost:5000/products?source=json (still works)
- http://localhost:5000/products?source=csv (still works)
- http://localhost:5000/products?source=sql&id=1 (filter by id)
- http://localhost:5000/products?source=invalid (error)

Expected:
- All three sources (json, csv, sql) work correctly
- Filtering by id works for all sources
- Invalid sources show appropriate error messages

## Stopping Flask Apps

Press `Ctrl+C` in the terminal to stop the Flask development server.

## Common Issues

1. **Port already in use**: If you get an error about port 5000, either:
   - Stop the previous Flask app (Ctrl+C)
   - Or change the port in the code: `app.run(debug=True, port=5001)`

2. **Template not found**: Make sure you're running the Flask app from the project directory

3. **Module not found**: Ensure Flask is installed: `pip install Flask`

4. **Database not found**: Run `create_database.py` before testing task 4

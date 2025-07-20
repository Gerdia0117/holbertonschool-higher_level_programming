# Python - Server-Side Rendering

This project demonstrates server-side rendering (SSR) techniques using Python Flask framework with Jinja templating engine. The project covers various aspects of web development including template rendering, data handling from multiple sources, and dynamic content generation.

## Project Overview

Server-side rendering is a powerful technique where web pages are generated on the server and sent to the client as fully formed HTML. This project implements SSR using Flask and Jinja, showcasing:

- Template-based HTML generation
- Dynamic content rendering with loops and conditionals
- Multi-format data source integration (JSON, CSV, SQLite)
- Error handling and edge case management
- Reusable component design

## Learning Objectives

By completing this project, you will understand:
- The concepts of server-side rendering vs client-side rendering
- Benefits of using server-side rendering in web development
- Implementation of SSR in Python using Flask framework
- Jinja templating engine for dynamic HTML generation
- Reading and displaying data from various sources (JSON, CSV, SQLite)
- Handling dynamic content and user inputs in web applications
- Query parameter processing and data filtering
- Database integration with SQLite
- Error handling and graceful failure management

## Project Structure

```
python-server_side_rendering/
├── task_00_intro.py          # Template system with error handling
├── task_01_jinja.py          # Basic Flask app with Jinja templates
├── task_02_logic.py          # Dynamic templates with loops/conditionals
├── task_03_files.py          # JSON/CSV data source integration
├── task_04_db.py             # SQLite database integration
├── templates/
│   ├── index.html            # Home page template
│   ├── about.html            # About page template
│   ├── contact.html          # Contact page template
│   ├── items.html            # Dynamic items display
│   ├── product_display.html  # Product data table display
│   ├── header.html           # Reusable header component
│   └── footer.html           # Reusable footer component
├── data files/
│   ├── template.txt          # Template for task 0
│   ├── items.json            # Items data for dynamic display
│   ├── products.json         # Product data in JSON format
│   ├── products.csv          # Product data in CSV format
│   └── products.db           # SQLite database with products
├── create_database.py        # Database setup script
└── README.md                 # Project documentation
```

## Tasks Description

### Task 0: Creating a Simple Templating Program
**File**: `task_00_intro.py`

- **Objective**: Implement string templating in Python with file operations
- **Features**: 
  - Template placeholder replacement (`{name}`, `{event_title}`, etc.)
  - Sequential output file generation (`output_1.txt`, `output_2.txt`, etc.)
  - Comprehensive error handling for edge cases
  - Input validation for template and attendees parameters
- **Error Handling**: Empty templates, empty data, missing values (replaced with "N/A")

### Task 1: Creating a Basic HTML Template in Flask
**File**: `task_01_jinja.py`

- **Objective**: Build basic Flask application with Jinja templates
- **Features**:
  - Flask routes for multiple pages (`/`, `/about`, `/contact`)
  - Jinja template rendering with `render_template()`
  - Reusable header and footer components
  - Navigation system across all pages
- **Templates**: Basic HTML structure with shared components

### Task 2: Creating Dynamic Templates with Loops and Conditions
**File**: `task_02_logic.py`

- **Objective**: Implement dynamic content with Jinja control structures
- **Features**:
  - JSON data reading and parsing
  - Jinja loops (`{% for %}`) for iterating over data
  - Conditional rendering (`{% if %}`) for empty states
  - Dynamic list generation from JSON data
- **Route**: `/items` - displays items from `items.json`

### Task 3: Displaying Data from JSON or CSV Files
**File**: `task_03_files.py`

- **Objective**: Multi-format data source integration with query parameters
- **Features**:
  - JSON and CSV file reading capabilities
  - Query parameter processing (`?source=json&id=1`)
  - Data filtering by product ID
  - Comprehensive error handling for invalid sources/IDs
  - Tabular data display with proper formatting
- **Route**: `/products?source=json|csv&id=optional`
- **Error Cases**: "Wrong source", "Product not found"

### Task 4: Extending to Include SQLite Database
**File**: `task_04_db.py`

- **Objective**: Add database integration as third data source
- **Features**:
  - SQLite database connection and querying
  - Extended query parameter support (`?source=sql`)
  - Database error handling
  - Unified template for all data sources
- **Database**: `products.db` with Products table
- **Route**: `/products?source=json|csv|sql&id=optional`

## Installation and Setup

### Prerequisites
- Python 3.x
- Flask framework

### Installation
```bash
# Install Flask (if not already installed)
pip install Flask

# Or using system package manager
sudo apt-get install python3-flask
```

### Database Setup
```bash
# Create and populate SQLite database
python3 create_database.py
```

## Running the Applications

Each task has its own Flask application:

```bash
# Task 1: Basic templates
python3 task_01_jinja.py

# Task 2: Dynamic templates
python3 task_02_logic.py

# Task 3: JSON/CSV data sources
python3 task_03_files.py

# Task 4: All data sources including SQLite
python3 task_04_db.py
```

All applications run on `http://localhost:5000`

## API Endpoints

### Common Routes (All Tasks)
- `GET /` - Home page
- `GET /about` - About page
- `GET /contact` - Contact page

### Task-Specific Routes

#### Task 2+
- `GET /items` - Display items from JSON file

#### Task 3+
- `GET /products?source=json` - All products from JSON
- `GET /products?source=csv` - All products from CSV
- `GET /products?source=json&id=1` - Single product by ID from JSON
- `GET /products?source=csv&id=999` - Invalid ID (shows error)
- `GET /products?source=xml` - Invalid source (shows error)

#### Task 4
- `GET /products?source=sql` - All products from SQLite
- `GET /products?source=sql&id=1` - Single product by ID from SQLite

## Data Formats

### JSON Format (`products.json`)
```json
[
    {
        "id": 1,
        "name": "Laptop",
        "category": "Electronics",
        "price": 799.99
    }
]
```

### CSV Format (`products.csv`)
```csv
id,name,category,price
1,Laptop,Electronics,799.99
2,Coffee Mug,Home Goods,15.99
```

### SQLite Database Structure
```sql
CREATE TABLE Products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
);
```

## Key Features Implemented

### Template System
- **Jinja Template Engine**: Dynamic HTML generation
- **Template Inheritance**: Reusable components (header/footer)
- **Control Structures**: Loops, conditionals, and filters
- **Template Includes**: Modular template design

### Data Handling
- **Multi-Source Support**: JSON, CSV, SQLite database
- **Type Conversion**: Proper data type handling
- **Query Parameters**: Dynamic filtering and source selection
- **Error Handling**: Graceful failure for missing/invalid data

### Flask Features
- **Routing**: Multiple endpoints with parameter handling
- **Request Processing**: Query parameter extraction and validation
- **Template Rendering**: Server-side HTML generation
- **Debug Mode**: Development-friendly error reporting

## Error Handling

The application handles various error scenarios:

### Task 0 (Templating)
- Empty template strings
- Empty attendee lists
- Invalid input types
- Missing placeholder values

### Tasks 1-4 (Flask Applications)
- File not found errors
- Invalid JSON/CSV format
- Database connection errors
- Invalid query parameters
- Missing product IDs
- Invalid data sources

## Testing Scenarios

### Functional Testing
1. **Valid Data Sources**: Test with JSON, CSV, and SQL sources
2. **Data Filtering**: Test ID-based filtering with valid/invalid IDs
3. **Error Cases**: Test invalid sources, missing files, corrupt data
4. **Edge Cases**: Empty datasets, malformed queries

### URL Testing Examples
```bash
# Valid requests
curl "http://localhost:5000/products?source=json"
curl "http://localhost:5000/products?source=csv&id=1"
curl "http://localhost:5000/products?source=sql"

# Error cases
curl "http://localhost:5000/products?source=xml"        # Wrong source
curl "http://localhost:5000/products?source=json&id=999" # Product not found
```

## Technical Implementation Details

### Flask Configuration
- Debug mode enabled for development
- Port 5000 (configurable)
- Template folder: `templates/`
- Static files support

### Database Integration
- SQLite3 for lightweight database operations
- Connection pooling and proper cleanup
- Parameterized queries for security
- Error handling for database operations

### File Processing
- JSON: Using `json` module with error handling
- CSV: Using `csv.DictReader` for structured parsing
- Template files: String replacement with validation

## Security Considerations

- Input validation for all user parameters
- Parameterized database queries
- File access restrictions
- Error message sanitization
- No direct code execution from user input

## Performance Considerations

- File caching could be implemented for production
- Database connection pooling
- Template caching with Jinja
- Static file serving optimization

## Repository Information

- **GitHub Repository**: holbertonschool-higher_level_programming
- **Directory**: python-server_side_rendering
- **Language**: Python 3.x
- **Framework**: Flask with Jinja2 templating
- **Database**: SQLite3

## Author

Holberton School Project - Python Server-Side Rendering

---

*This project demonstrates comprehensive server-side rendering techniques using modern Python web development practices with Flask and Jinja templating.*

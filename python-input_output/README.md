# Python - Input/Output

This project covers file handling and JSON serialization/deserialization in Python.

## Learning Objectives
- File operations: opening, reading, writing, and closing files
- Using `with` statement for automatic file handling
- Working with file cursor positions
- JSON serialization (Python objects to JSON strings)
- JSON deserialization (JSON strings to Python objects)
- Accessing command line arguments

## Key Concepts
### File Handling
- `open()`: Open files in different modes (read 'r', write 'w', append 'a')
- File methods: `read()`, `readline()`, `write()`, `seek()`, `tell()`
- Context managers (`with` statement) for automatic resource cleanup

### JSON Operations
- `json.dumps()`: Convert Python object to JSON string
- `json.loads()`: Convert JSON string to Python object
- `json.dump()`: Write JSON data to file
- `json.load()`: Read JSON data from file

### Command Line Arguments
- Access via `sys.argv` list

## Requirements
- Python 3.8.5
- Files must be executable and pass `pycodestyle` validation
- Proper documentation for all modules, classes, and functions

## Usage
Run Python scripts directly:
```bash
./script_name.py

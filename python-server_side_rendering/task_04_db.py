from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file(filename):
    """
    Read and parse data from a JSON file.
    Returns list of products or empty list if error.
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv_file(filename):
    """
    Read and parse data from a CSV file.
    Returns list of dictionaries representing products.
    """
    try:
        products = []
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert id and price to appropriate types
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(product)
        return products
    except (FileNotFoundError, ValueError, KeyError):
        return []

def read_sqlite_db(filename):
    """
    Read and parse data from an SQLite database.
    Returns list of products or empty list if error.
    """
    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        products = [
            {
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3],
            }
            for row in rows
        ]
        conn.close()
        return products
    except sqlite3.Error:
        return []

def filter_products_by_id(products, product_id):
    """
    Filter products by a specific ID.
    Returns a single product in a list if found, empty list otherwise.
    """
    try:
        product_id = int(product_id)
        filtered = [p for p in products if p['id'] == product_id]
        return filtered
    except (ValueError, TypeError):
        return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    
    return render_template('items.html', items=items_list)

@app.route('/products')
def display_products():
    # Get query parameters
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Check if source parameter is valid
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', 
                             error_message="Wrong source", 
                             products=None)
    
    # Read data based on source
    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    elif source == 'sql':
        products = read_sqlite_db('products.db')
    else:
        products = []
    
    # Filter by ID if provided
    if product_id is not None:
        filtered_products = filter_products_by_id(products, product_id)
        if not filtered_products:
            return render_template('product_display.html', 
                                 error_message="Product not found", 
                                 products=None)
        products = filtered_products
    
    return render_template('product_display.html', 
                         products=products, 
                         error_message=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

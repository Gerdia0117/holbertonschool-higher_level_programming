#!/usr/bin/python3
"""
Flask application displaying data from JSON or CSV files.
"""
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json_file(filepath):
    """Read and parse JSON file."""
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv_file(filepath):
    """Read and parse CSV file."""
    try:
        products = []
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert id to int and price to float
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
        return products
    except (FileNotFoundError, ValueError, KeyError):
        return []


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render the items page with data from JSON file."""
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    """Render the products page with data from JSON or CSV."""
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    # Read data based on source
    if source == 'json':
        products_list = read_json_file('products.json')
    else:  # source == 'csv'
        products_list = read_csv_file('products.csv')
    
    # Filter by id if provided
    if product_id is not None:
        filtered_products = [p for p in products_list if p['id'] == product_id]
        if not filtered_products:
            return render_template('product_display.html', 
                                 error="Product not found")
        products_list = filtered_products
    
    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

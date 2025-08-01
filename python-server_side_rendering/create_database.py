import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Clear existing data first
    cursor.execute('DELETE FROM Products')
    
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'Desk Chair', 'Furniture', 249.50),
        (4, 'Notebook', 'Stationery', 5.99),
        (5, 'Headphones', 'Electronics', 129.00)
    ''')
    conn.commit()
    conn.close()
    print("Database 'products.db' created and populated successfully!")

if __name__ == '__main__':
    create_database()

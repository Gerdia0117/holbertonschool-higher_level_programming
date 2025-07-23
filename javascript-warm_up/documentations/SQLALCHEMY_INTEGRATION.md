# SQLAlchemy Integration Guide

This document provides a detailed overview of integrating SQLAlchemy with Flask applications, covering configuration and usage for seamless database interactions.

## Overview

SQLAlchemy is a powerful ORM for Python that provides a full suite of tools for database interactions, including connection pooling, declarative models, and more.

## Configuration

### Installing SQLAlchemy

```bash
pip install Flask-SQLAlchemy
```

### Setting Up Flask App with SQLAlchemy

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
```

## Defining Models

### Basic Model Example

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
```

## CRUD Operations

### Create

```python
new_user = User(username='john_doe', email='john@example.com')
db.session.add(new_user)
db.session.commit()
```

### Read

```python
user = User.query.filter_by(username='john_doe').first()
```

### Update

```python
user.email = 'john.doe@example.com'
db.session.commit()
```

### Delete

```python
db.session.delete(user)
db.session.commit()
```

## Querying Data

SQLAlchemy provides a flexible query structure similar to SQL, with a full suite of filters, joins, and aggregation functions.

### Common Query Patterns

- **Filter**: `User.query.filter_by(username='john_doe').all()`
- **Joins**: `db.session.query(User).join(Address).filter(User.id == Address.user_id).all()`
- **Order By**: `User.query.order_by(User.username).all()`

## Migrations

To handle database schema changes over time, use Flask-Migrate.

### Setting Up Migrations

```bash
pip install Flask-Migrate
```

### Running Migrations

```python
from flask_migrate import Migrate
migrate = Migrate(app, db)
```

```bash
flask db init
flask db migrate
flask db upgrade
```

## Best Practices

- **Use Models** for all database interactions to utilize ORM features
- **Modularize** configuration for different environments (dev, prod)
- **Secure Configuration** with environment variables (access strings, secrets)
- **Utilize Lazy Loading** where possible for performance optimization

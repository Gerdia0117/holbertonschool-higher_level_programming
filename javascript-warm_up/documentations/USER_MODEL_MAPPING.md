# User Model Mapping

This document provides a comprehensive guide to modeling users in a database using Flask and SQLAlchemy.

## Overview

The user model is an essential component for applications requiring authentication, authorization, and user profile management.

## Key Components

- **User ID**: Unique identifier for each user
- **Email**: Used for user identification and communication
- **Password Hash**: Stores a hashed password for security
- **Authentication Tokens**: For maintaining user sessions

## Implementation

### Basic User Model

```python
from flask_sqlalchemy import SQLAlchemy
import bcrypt

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.LargeBinary(128))

    def set_password(self, password):
        """Hash and set password."""
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password_bytes, salt)

    def check_password(self, password):
        """Verify password against hash."""
        password_bytes = password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, self.password_hash)

    @staticmethod
    def create_user(username, email, password):
        """Create a new user instance."""
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user
```

### Advanced Features

- **Profiles**: Extend user data with additional tables such as profiles, using a one-to-one relationship
- **Roles**: Implement role-based access control (RBAC) by associating roles with users
- **Activity Logs**: Track user activities for auditing and analytics

## CRUD Operations

### Create

```python
new_user = User.create_user('john_doe', 'john@example.com', 'securepassword')
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
User.query.filter_by(username='john_doe').delete()
db.session.commit()
```

## Best Practices

- **Use Unique Identifiers** for fields like username and email
- **Hash Passwords** before storing
- **Keep Implementation Modular** to easily add new features
- **Adopt Strong Security Practices** for handling sensitive information

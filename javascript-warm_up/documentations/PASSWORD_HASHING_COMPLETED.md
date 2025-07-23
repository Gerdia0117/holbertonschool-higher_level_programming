# Password Hashing - Complete Implementation

This document covers the complete implementation of secure password hashing in Python applications using industry best practices.

## Overview

Password hashing is a critical security measure that transforms plain-text passwords into irreversible hash values, protecting user credentials even if the database is compromised.

## Implementation

### Dependencies

```bash
pip install bcrypt
# Alternative: pip install werkzeug (includes password hashing)
```

### Using bcrypt (Recommended)

```python
import bcrypt

class User:
    def __init__(self, email, password):
        self.email = email
        self.password_hash = self.hash_password(password)
    
    def hash_password(self, password):
        """Hash a password with a random salt."""
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password_bytes, salt)
    
    def check_password(self, password):
        """Check if the provided password matches the hash."""
        password_bytes = password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, self.password_hash)
    
    def update_password(self, new_password):
        """Update user password with a new hash."""
        self.password_hash = self.hash_password(new_password)
```

### Using Werkzeug Security

```python
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, email, password):
        self.email = email
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check if the provided password matches the hash."""
        return check_password_hash(self.password_hash, password)
    
    def update_password(self, new_password):
        """Update user password with a new hash."""
        self.password_hash = generate_password_hash(new_password)
```

### SQLAlchemy Integration

```python
from flask_sqlalchemy import SQLAlchemy
import bcrypt

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.LargeBinary(128), nullable=False)
    
    def set_password(self, password):
        """Hash and set password."""
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password_bytes, salt)
    
    def check_password(self, password):
        """Verify password against hash."""
        password_bytes = password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, self.password_hash)
    
    @classmethod
    def create_user(cls, email, password):
        """Create a new user with hashed password."""
        user = cls(email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user
```

### Registration Route Example

```python
from flask import request, jsonify

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    # Validate input
    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400
    
    # Check if user exists
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'User already exists'}), 409
    
    # Validate password strength
    if len(password) < 8:
        return jsonify({'error': 'Password must be at least 8 characters'}), 400
    
    # Create user
    user = User.create_user(email, password)
    
    return jsonify({
        'message': 'User created successfully',
        'user_id': user.id
    }), 201
```

### Login Route Example

```python
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user = User.query.filter_by(email=email).first()
    
    if user and user.check_password(password):
        # Generate JWT token or session
        return jsonify({'message': 'Login successful'}), 200
    
    return jsonify({'error': 'Invalid credentials'}), 401
```

### Password Change Implementation

```python
@app.route('/change-password', methods=['POST'])
@jwt_required()  # Assuming JWT authentication
def change_password():
    data = request.get_json()
    current_password = data.get('current_password')
    new_password = data.get('new_password')
    
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user.check_password(current_password):
        return jsonify({'error': 'Current password is incorrect'}), 400
    
    if len(new_password) < 8:
        return jsonify({'error': 'New password must be at least 8 characters'}), 400
    
    user.set_password(new_password)
    db.session.commit()
    
    return jsonify({'message': 'Password updated successfully'}), 200
```

## Security Best Practices

### Password Validation

```python
import re

def validate_password(password):
    """Validate password strength."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit"
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character"
    
    return True, "Password is valid"
```

## Key Points

- **Never store plain-text passwords**
- **Use salt** to prevent rainbow table attacks
- **Choose appropriate cost factors** for bcrypt (12-15 is recommended)
- **Implement rate limiting** for login attempts
- **Use HTTPS** to protect passwords in transit
- **Validate password strength** on the client and server side
- **Consider password breach checking** using services like HaveIBeenPwned API

## Common Mistakes to Avoid

1. Using weak hashing algorithms (MD5, SHA1)
2. Not using salt
3. Storing salt separately from hash
4. Not validating password strength
5. Logging passwords in application logs
6. Not implementing account lockout mechanisms

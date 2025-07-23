# JWT Authentication - Complete Implementation

This document provides a comprehensive guide to implementing JWT (JSON Web Token) authentication in Flask applications.

## Overview

JWT authentication provides a stateless way to authenticate users by using digitally signed tokens that contain user information and claims.

## Implementation

### Dependencies

```bash
pip install PyJWT flask-jwt-extended
```

### Configuration

```python
from flask_jwt_extended import JWTManager
from datetime import timedelta

app.config['JWT_SECRET_KEY'] = 'your-secret-string'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)

jwt = JWTManager(app)
```

### Authentication Routes

```python
from flask import request, jsonify
from flask_jwt_extended import (
    jwt_required, create_access_token, create_refresh_token,
    get_jwt_identity, get_jwt
)

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    
    user = User.query.filter_by(email=email).first()
    
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        return jsonify({
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': user.to_dict()
        })
    
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user)
    return jsonify({'access_token': new_token})

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({'logged_in_as': current_user})
```

### Token Blacklisting

```python
blacklisted_tokens = set()

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    return jwt_payload['jti'] in blacklisted_tokens

@app.route('/logout', methods=['DELETE'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    blacklisted_tokens.add(jti)
    return jsonify({'message': 'Successfully logged out'})
```

### Error Handlers

```python
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({'message': 'Token has expired'}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({'message': 'Invalid token'}), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({'message': 'Token is required'}), 401
```

## Usage Examples

### Client-side Implementation

```javascript
// Login
const response = await fetch('/login', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        email: 'user@example.com',
        password: 'password123'
    })
});

const data = await response.json();
localStorage.setItem('access_token', data.access_token);

// Making authenticated requests
const protectedResponse = await fetch('/protected', {
    headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
    }
});
```

## Best Practices

- Use strong secret keys
- Implement token refresh mechanisms
- Set appropriate expiration times
- Implement token blacklisting for logout
- Use HTTPS in production
- Store tokens securely on the client side

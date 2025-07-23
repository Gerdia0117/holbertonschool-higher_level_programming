# Application Factory Pattern - Complete Implementation

This document covers the complete implementation of the Application Factory pattern in Flask applications.

## Overview

The Application Factory pattern is a design pattern used to create Flask applications in a flexible and modular way. This pattern allows you to create multiple instances of your application with different configurations.

## Implementation

### Basic Factory Structure

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
```

### Configuration Management

```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///app-dev.db'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///app.db'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```

## Benefits

- **Testability**: Easy to create app instances for testing
- **Flexibility**: Different configurations for different environments
- **Modularity**: Clean separation of concerns
- **Scalability**: Easy to extend and modify

## Usage

```python
from app import create_app

app = create_app('development')

if __name__ == '__main__':
    app.run()
```

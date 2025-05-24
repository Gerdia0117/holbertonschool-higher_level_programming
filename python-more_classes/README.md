# Python Object-Oriented Programming Project

## Resources
### Required Reading/Watching
- [Object Oriented Programming](https://python.swaroopch.com/oop.html) (Stop before Inheritance)
- [Python OOP Concepts](https://python-course.eu/oop/object-oriented-programming.php) (Focus on:
  - General Introduction
  - First-class Everything
  - A Minimal Class in Python
  - Attributes
  - Methods
  - The `__init__` Method
  - Data Abstraction, Data Encapsulation, and Information Hiding
  - `__str__` and `__repr__` Methods
  - Public, Protected, and Private Attributes
  - Destructor)
- [Class and Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)
- [Classmethods and Staticmethods](https://realpython.com/instance-class-and-static-methods-demystified/)
- [Properties vs. Getters/Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php) (Focus on "Public instead of Private Attributes")
- [`__str__` vs `__repr__`](https://www.geeksforgeeks.org/str-vs-repr-in-python/)

## Learning Objectives
### General OOP Concepts
- Understand why Python programming is awesome
- Explain Object-Oriented Programming (OOP) principles
- Describe "first-class everything" in Python
- Differentiate between classes, objects, and instances
- Understand `self` in Python classes

### Attributes and Methods
- Implement and use:
  - Public, protected, and private attributes
  - Instance methods
  - The special `__init__` method
  - Data Abstraction, Encapsulation, and Information Hiding
- Differentiate between attributes and properties
- Implement Pythonic getters and setters

### Special Methods
- Implement and understand:
  - `__str__` and `__repr__` methods
  - Differences between `__str__` and `__repr__`
  - Class attributes vs instance attributes
  - Class methods and static methods

### Advanced Concepts
- Dynamically create new attributes
- Bind attributes to objects and classes
- Understand `__dict__` of classes and instances
- Explain Python's attribute lookup mechanism
- Use `getattr()` function effectively

## Requirements
### General
- **Editors**: vi, vim, emacs
- **Execution Environment**: Ubuntu 20.04 LTS with Python 3.8.5
- **File Requirements**:
  - All files must end with a new line
  - First line must be `#!/usr/bin/python3`
  - Must be executable
  - Length checked with `wc`

### Code Quality
- **Style Guide**: pycodestyle (version 2.7.*)
- **Documentation**:
  - Mandatory for all modules, classes, and methods
  - Verified with:
    ```bash
    python3 -c 'print(__import__("my_module").__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    ```
  - Documentation must be meaningful sentences (not just single words)

### Testing
- Include comprehensive test cases
- Follow Test-Driven Development principles
- Ensure all edge cases are covered

## Project Structure
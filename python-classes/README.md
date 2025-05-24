# Python Matrix Division Module

## Background Context
This project is part of the Holberton School curriculum on Python programming and Test-Driven Development. The goal is to implement a function that divides all elements of a matrix while following strict coding standards and documentation requirements.

## Resources
Before working on this project, review these key concepts:
- [Object Oriented Programming](https://python.swaroopch.com/oop.html) (Stop before Inheritance)
- [Python OOP Concepts](https://python-course.eu/oop/object-oriented-programming.php)
- [Properties vs Getters/Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
- [Python Classes/Objects](https://www.w3schools.com/python/python_classes.asp)

## Learning Objectives
By completing this project, you'll understand:
- Object-Oriented Programming fundamentals
- Python class and object implementation
- Proper documentation standards
- Type checking and error handling
- Test-Driven Development practices

## Project Requirements
### Function: `matrix_divided(matrix, div)`
Divides all elements of a matrix by a given number.

**Parameters:**
- `matrix`: List of lists containing integers/floats
- `div`: Number to divide by (integer/float)

**Returns:**
- New matrix with elements divided by `div` (rounded to 2 decimal places)

**Raises:**
- `TypeError`: If matrix isn't list of lists of numbers, or rows are different sizes
- `ZeroDivisionError`: If div equals 0

### Example Usage
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
# Output: [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
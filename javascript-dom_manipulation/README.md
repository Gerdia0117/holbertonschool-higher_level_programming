# JavaScript - DOM Manipulation

This project contains JavaScript scripts that demonstrate various DOM (Document Object Model) manipulation techniques, event handling, and API interactions using modern JavaScript features.

## Project Overview

This repository includes 8 different JavaScript exercises that cover:
- DOM element selection and manipulation
- Event handling (click events)
- Dynamic content creation and modification
- Fetch API for external data retrieval
- Working with promises and asynchronous JavaScript

## Learning Objectives

At the end of this project, you should be able to explain:
- How to select HTML elements in JavaScript
- What are the differences between ID, class, and tag name selectors
- How to modify an HTML element's style, content, or attributes
- How to modify the DOM and add/remove elements
- How to make HTTP requests with the Fetch API
- How to bind event listeners to DOM elements
- How to work with promises and handle asynchronous operations

## Files Description

### Task 0: Color Me
- **File**: `0-script.js`, `0-main.html`
- **Description**: Updates the text color of the header element to red (#FF0000)
- **Concept**: Basic DOM selection and style manipulation

### Task 1: Click and turn red
- **File**: `1-script.js`, `1-main.html`
- **Description**: Updates the text color of the header element to red when clicking on a specific div
- **Concept**: Event handling and DOM manipulation

### Task 2: Add CSS class
- **File**: `2-script.js`, `2-main.html`
- **Description**: Adds the CSS class 'red' to the header element when clicking on a div
- **Concept**: CSS class manipulation

### Task 3: Toggle classes
- **File**: `3-script.js`, `3-main.html`
- **Description**: Toggles the header element class between 'red' and 'green' when clicking on a div
- **Concept**: Class toggling and conditional logic

### Task 4: List of elements
- **File**: `4-script.js`, `4-main.html`
- **Description**: Adds a new `<li>Item</li>` element to a list when clicking on a div
- **Concept**: Dynamic element creation and DOM insertion

### Task 5: Change the text
- **File**: `5-script.js`, `5-main.html`
- **Description**: Updates the header text to "New Header!!!" when clicking on a div
- **Concept**: Text content manipulation

### Task 6: Star Wars character
- **File**: `6-script.js`, `6-main.html`
- **Description**: Fetches and displays a Star Wars character name using the Fetch API
- **Concept**: API requests, promises, and asynchronous JavaScript
- **API**: `https://swapi-api.hbtn.io/api/people/5/?format=json`

### Task 7: Star Wars movies
- **File**: `7-script.js`, `7-main.html`
- **Description**: Fetches and lists all Star Wars movie titles
- **Concept**: API requests with array handling and dynamic list creation
- **API**: `https://swapi-api.hbtn.io/api/films/?format=json`

### Task 8: Say Hello!
- **File**: `8-script.js`, `8-main.html`
- **Description**: Fetches French translation of "hello" and displays it (script loaded from head)
- **Concept**: DOM ready events, API requests, and script positioning
- **API**: `https://hellosalut.stefanbohacek.dev/?lang=fr`

## Technical Requirements

- All scripts are written in JavaScript ES6+
- No use of `var` keyword
- Scripts use modern features like `const`, `let`, arrow functions, and template literals where appropriate
- All scripts include proper error handling
- HTML files are W3C compliant
- Scripts work in modern browsers (Chrome, Firefox, Safari, Edge)

## Key JavaScript Concepts Used

### DOM Manipulation
```javascript
// Element selection
document.getElementById('elementId')
document.querySelector('.className')
document.querySelector('tagName')

// Content modification
element.textContent = 'new text'
element.style.color = 'red'
element.classList.add('className')
element.classList.toggle('className')
```

### Event Handling
```javascript
// Adding event listeners
element.addEventListener('click', function() {
    // Event handling code
});
```

### Dynamic Element Creation
```javascript
// Creating and appending elements
const newElement = document.createElement('tagName');
newElement.textContent = 'content';
parentElement.appendChild(newElement);
```

### Fetch API and Promises
```javascript
// Making API requests
fetch('https://api.example.com/data')
    .then(response => response.json())
    .then(data => {
        // Handle data
    })
    .catch(error => {
        console.error('Error:', error);
    });
```

### DOM Ready Event
```javascript
// Ensuring DOM is loaded (for scripts in head)
document.addEventListener('DOMContentLoaded', function() {
    // Code that needs DOM to be ready
});
```

## How to Test

1. Open any of the HTML files in a modern web browser
2. Interact with the page elements as described in each task
3. Check browser developer console for any errors
4. For API-based tasks (6, 7, 8), ensure you have internet connectivity

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

All scripts use modern JavaScript features and the Fetch API, which require recent browser versions.

## Repository Information

- **GitHub repository**: holbertonschool-higher_level_programming
- **Directory**: javascript-dom_manipulation
- **Language**: JavaScript (ES6+)
- **Environment**: Web Browser

## Author

Holberton School Project - JavaScript DOM Manipulation

---

*This project is part of the Holberton School curriculum and demonstrates fundamental JavaScript DOM manipulation techniques and modern web development practices.*

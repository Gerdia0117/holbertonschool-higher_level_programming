// Get the element with id 'red_header'
const redHeaderElement = document.getElementById('red_header');

// Get the header element
const headerElement = document.querySelector('header');

// Add click event listener to the red_header element
redHeaderElement.addEventListener('click', function() {
  // Change the header text color to red
  headerElement.style.color = '#FF0000';
});
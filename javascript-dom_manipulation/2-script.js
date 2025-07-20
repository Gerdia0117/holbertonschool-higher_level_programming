// Get the element with id 'red_header'
const redHeaderElement = document.getElementById('red_header');

// Get the header element
const headerElement = document.querySelector('header');

// Add click event listener to the red_header element
redHeaderElement.addEventListener('click', function() {
  // Add the 'red' class to the header element
  headerElement.classList.add('red');
});
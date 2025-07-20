// Get the element with id 'toggle_header'
const toggleHeaderElement = document.getElementById('toggle_header');

// Get the header element
const headerElement = document.querySelector('header');

// Add click event listener to the toggle_header element
toggleHeaderElement.addEventListener('click', function() {
  // Check if header currently has the 'red' class
  if (headerElement.classList.contains('red')) {
    // If it has 'red', remove it and add 'green'
    headerElement.classList.remove('red');
    headerElement.classList.add('green');
  } else {
    // If it doesn't have 'red' (so it has 'green'), remove 'green' and add 'red'
    headerElement.classList.remove('green');
    headerElement.classList.add('red');
  }
});

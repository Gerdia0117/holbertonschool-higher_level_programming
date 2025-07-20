// Wait for the DOM to be fully loaded before executing
document.addEventListener('DOMContentLoaded', function() {
  // Fetch the French translation of "hello"
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      // Get the element with id 'hello'
      const helloElement = document.getElementById('hello');
      
      // Display the translation in the hello element
      helloElement.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching translation:', error);
    });
});

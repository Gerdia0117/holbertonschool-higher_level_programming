// Get the element with id 'update_header' and add click event listener
document.getElementById('update_header').addEventListener('click', function() {
  // Get the header element
  const header = document.querySelector('header');
  
  // Update the text content to 'New Header!!!'
  header.textContent = 'New Header!!!';
});

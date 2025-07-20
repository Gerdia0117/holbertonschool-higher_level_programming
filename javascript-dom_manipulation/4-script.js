// Get the element with id 'add_item' and add click event listener
document.getElementById('add_item').addEventListener('click', function() {
  // Create a new li element
  const newItem = document.createElement('li');
  
  // Set the text content to 'Item'
  newItem.textContent = 'Item';
  
  // Get the ul element with class 'my_list'
  const list = document.querySelector('ul.my_list');
  
  // Append the new li element to the list
  list.appendChild(newItem);
});
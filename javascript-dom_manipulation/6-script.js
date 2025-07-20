// Fetch character data from the Star Wars API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    // Get the element with id 'character'
    const characterElement = document.getElementById('character');
    
    // Display the character name
    characterElement.textContent = data.name;
  })
  .catch(error => {
    console.error('Error fetching character:', error);
  });

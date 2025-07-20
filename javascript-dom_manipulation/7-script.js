// Fetch all Star Wars movies from the API
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    // Get the ul element with id 'list_movies'
    const moviesList = document.getElementById('list_movies');
    
    // Loop through each movie in the results array
    data.results.forEach(movie => {
      // Create a new li element
      const listItem = document.createElement('li');
      
      // Set the text content to the movie title
      listItem.textContent = movie.title;
      
      // Append the li element to the ul
      moviesList.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error('Error fetching movies:', error);
  });

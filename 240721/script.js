document.getElementById('fetch-joke-button').addEventListener('click', fetchJoke);

function fetchJoke() {
  fetch('https://official-joke-api.appspot.com/random_joke')
      .then(response => response.json())
      .then(data => {
          document.getElementById('joke-display').innerText = `${data.setup} - ${data.punchline}`;
      })
      .catch(error => {
          console.error('Error fetching joke:', error);
      });
}
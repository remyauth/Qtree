fetch('data/figures.json')
  .then(response => response.json())
  .then(data => {
    console.log("Loaded data:", data);

    // Basic placeholder to show something on screen
    const container = document.getElementById('timeline');
    data.forEach(person => {
      const entry = document.createElement('div');
      entry.innerHTML = `<strong>${person.name}</strong> (${person.birth}–${person.death})<br>${person.bio}`;
      container.appendChild(entry);
    });
  })
  .catch(error => {
    console.error("Error loading data:", error);
  });



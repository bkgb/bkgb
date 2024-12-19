

//
// Script for loading thumbnail gallery
//

fetch('links.json')
  .then(response => response.json())
  .then(data => {
    const gallery = document.getElementById('gallery');
    data.forEach(item => {
      const a = document.createElement('a');
      a.href = item.link;
      a.target = '_blank'; // Open link in a new tab

      const img = document.createElement('img');
      img.src = item.thumbnail;
      img.alt = 'Thumbnail';  // You can also add item.title if available for alt

      a.appendChild(img);
      gallery.appendChild(a);
    });
  })
  .catch(error => console.error('Error loading links:', error));


fetch('https://bkgb.github.io/data')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok ' + response.statusText);
    }
    return response.json();
  })
  .then(data => {
    console.log('Data fetched successfully:', data);
  })
  .catch(error => {
    console.error('There has been a problem with your fetch operation:', error);
  });

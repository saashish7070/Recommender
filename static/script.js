document.addEventListener('DOMContentLoaded', function () {
   // First function
   fetch('/api/images')
       .then(response => response.json())
       .then(data => {
           const imageContainer = document.getElementById('image-container');
           
           const HTMLElems = data.map(product => {
               const customDiv = document.createElement('div')
               customDiv.id = product._id
               const img = document.createElement('img');
               img.src = product.images;
               img.width = 200; // Set the width to 600 pixels
               img.height = 250; // Set the height to 600 pixels
               customDiv.appendChild(img);
               return customDiv
           });
           HTMLElems.forEach( divs => imageContainer.appendChild(divs))
       })
       .catch(error => console.error('Error fetching images:', error));
});

// Second function
document.querySelectorAll('#image-container > div').forEach( productDivs => {
   productDivs.addEventListener('click', function() {
       fetch('/api/product', {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json',
           },
           body: JSON.stringify({ productId: productDivs.id }),
       }, ({ data }) => {
           const imageContainer = document.getElementById('image-container')
           imageContainer.innerHTML = ""

           const HTMLElems = data.map(product => {
               const customDiv = document.createElement('div')
               customDiv.id = product._id
               const img = document.createElement('img');
               img.src = product.images;
               img.width = 200; // Set the width to 600 pixels
               img.height = 250; // Set the height to 600 pixels
               customDiv.appendChild(img);
               return customDiv
           });
           HTMLElems.forEach( divs => imageContainer.appendChild(divs))
       } );
   });
});

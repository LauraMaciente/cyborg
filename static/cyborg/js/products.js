// script.js
function filterProducts(category) {
    const products = document.getElementsByClassName('product');
    
    for (let product of products) {
      if (category === 'all' || product.getAttribute('data-category') === category) {
        product.style.display = ''; // mostra o produto
      } else {
        product.style.display = 'none'; // esconde o produto
      }
    }
  }
  
  document.addEventListener('DOMContentLoaded', (event) => {
    // A função de filtragem já está pronta para ser usada pelos botões.
  });
  
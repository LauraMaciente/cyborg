function filterProducts(category) {
  const products = document.getElementsByClassName('product');
  
  for (let product of products) {
    if (category === 'all' || product.getAttribute('offer') === category) {
      product.style.display = ''; 
    } else {
      product.style.display = 'none'; 
    }
  }
}


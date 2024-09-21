// JavaScript for loading category products dynamically
function showCategory(categoryName) {
    const productContent = document.getElementById('product-content');
    productContent.innerHTML = `Loading products for ${categoryName}...`;

    fetch(`/get-products?category=${categoryName}`)
        .then(response => response.json())
        .then(data => {
            productContent.innerHTML = renderProducts(data);
        })
        .catch(error => {
            productContent.innerHTML = `Error loading products for ${categoryName}.`;
        });
}

function renderProducts(products) {
    return products.map(product => `
        <div class="single-product-item">
            <img src="${product.image}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>${product.description}</p>
            <p>Price: $${product.price}</p>
            <a href="#" class="cart-btn">Add to Cart</a>
        </div>
    `).join('');
}

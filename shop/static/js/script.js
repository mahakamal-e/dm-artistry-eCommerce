let currentSlide = 0;

function moveSlide(n) {
    const slides = document.querySelectorAll('.slides');
    currentSlide = (currentSlide + n + slides.length) % slides.length;
    slides.forEach((slide, index) => {
        slide.style.display = index === currentSlide ? 'block' : 'none';
    });
}

// Initialize the carousel
document.addEventListener('DOMContentLoaded', () => {
    moveSlide(0); // Show the first slide initially
    setInterval(() => moveSlide(1), 5000); // Automatic slide transition every 5 seconds
});

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

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.cart-btn').forEach(btn => {
        btn.addEventListener('click', (event) => {
            event.preventDefault();
            const productId = btn.getAttribute('data-product-id');
            fetch(`/add_to_cart/${productId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json'
                }
            }).then(response => {
                if (response.ok) {
                    updateCartIcon();
                }
            });
        });
    });
});

function updateCartIcon() {
    fetch('/cart_count/')
        .then(response => response.json())
        .then(data => {
            document.querySelector('#cart-icon').innerText = data.count;
        });
}


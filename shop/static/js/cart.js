
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



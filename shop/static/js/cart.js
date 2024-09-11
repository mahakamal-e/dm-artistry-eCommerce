// static/js/cart.js

document.addEventListener('DOMContentLoaded', function() {
    function updateCartCount() {
        fetch('/cart_count/')
            .then(response => response.json())
            .then(data => {
                document.querySelector('.count-badge').textContent = data.count || 0;
            });
    }

    // Call this function initially and after adding/removing items
    updateCartCount();

    // Example event listener for adding items (you can adapt this to your actual add-to-cart logic)
    document.querySelectorAll('.add-to-cart-button').forEach(button => {
        button.addEventListener('click', () => {
            updateCartCount();
        });
    });
});



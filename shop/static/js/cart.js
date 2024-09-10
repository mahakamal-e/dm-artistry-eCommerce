document.addEventListener('DOMContentLoaded', function() {
    function updateCartCount() {
        let url = '/cart/count/';  // Default URL for authenticated users

        // Optionally, determine if the user is logged in (if you have such data)
        if (userIsAuthenticated) {
            url = '/cart/count/';
        } else {
            url = '/cart/count-unauthenticated/';
        }

        fetch(url)
            .then(response => response.json())
            .then(data => {
                document.getElementById('cart-count').textContent = data.count;
            })
            .catch(error => console.error('Error fetching cart count:', error));
    }

    // Initial load
    updateCartCount();

    // Optional: Update cart count periodically (e.g., every minute)
    setInterval(updateCartCount, 60000);
});

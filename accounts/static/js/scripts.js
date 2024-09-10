document.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent default form submission

    var formData = new FormData(this);

    fetch(this.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': formData.get('csrfmiddlewaretoken') // Include CSRF token
        }
    }).then(response => {
        if (response.redirected) {
            window.location.href = response.url; // Redirect if response is a redirect
        } else {
            // Handle response errors or messages
        }
    });
});


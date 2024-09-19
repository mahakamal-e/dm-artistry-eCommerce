document.addEventListener('DOMContentLoaded', function () {
    // Automatically close alerts after 5 seconds
    var alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            $(alert).alert('close');
        }, 5000);
    });
});

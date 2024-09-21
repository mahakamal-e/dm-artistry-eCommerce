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
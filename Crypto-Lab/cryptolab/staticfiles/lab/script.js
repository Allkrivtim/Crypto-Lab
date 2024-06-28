document.addEventListener('DOMContentLoaded', function () {
    const fadeInElement = document.querySelector('.fade-in');
    if (fadeInElement) {
        fadeInElement.classList.remove('active');
    }

    function fadeOut(event) {
        event.preventDefault();
        fadeInElement.classList.add('active');
        setTimeout(function () {
            window.location.href = event.target.getAttribute('data-href');
        }, 250);
    }

    const pageLinks = document.querySelectorAll('.page-link');
    pageLinks.forEach(link => {
        link.addEventListener('click', fadeOut);
    });
});

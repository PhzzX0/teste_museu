document.addEventListener("DOMContentLoaded", () => {
    const menuBtn = document.querySelector(".menu-btn");
    const menuLinks = document.querySelector(".navbar-nav");

    menuBtn.addEventListener("click", () => {
        menuLinks.classList.toggle("active");
    });
});

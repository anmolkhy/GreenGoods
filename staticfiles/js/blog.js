document.addEventListener("DOMContentLoaded", () => {
  const navLinks = document.querySelectorAll("a");

  navLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();

      const targetId = link.getAttribute("href");
      const targetElement = document.querySelector(targetId);

      if (targetElement) {
        targetElement.scrollIntoView({
          behavior: "smooth", // Use "smooth" for smooth scrolling
          block: "start", // Align to the start of the target element
        });
      }
    });
  });
});

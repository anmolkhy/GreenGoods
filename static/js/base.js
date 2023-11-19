const scrollToFooter = () => {
  const footer = document.querySelector("#footer");
  footer.scrollIntoView({ behavior: "smooth" });
};

const link = document.querySelector('a[href="#footer"]');
link.addEventListener("click", scrollToFooter);

window.addEventListener("scroll", function () {
  const navbar = document.querySelector(".navbar");
  const scrolled = window.scrollY > navbar.offsetHeight;

  if (scrolled) {
    navbar.classList.add("navbar-visible");
    navbar.classList.add("sticky");
  } else {
    navbar.classList.remove("navbar-visible");
    navbar.classList.remove("sticky");
  }
});

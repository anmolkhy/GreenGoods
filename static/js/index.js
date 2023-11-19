const swiper = new Swiper(".swiper", {
  // Optional parameters
  autoHeight: true,
  loop: true,

  // If we need pagination
  pagination: {
    el: ".swiper-pagination",
  },

  // Navigation arrows
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  // And if we need scrollbar
  scrollbar: {
    el: ".swiper-scrollbar",
  },
});

function animateStats() {
  const statsItems = document.querySelectorAll(".stats-item");

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const statsNumber = entry.target.querySelector(".stats-number");
        const finalNumber = parseInt(statsNumber.innerText);
        let currentNumber = 0;

        const incrementNumber = setInterval(() => {
          if (currentNumber < finalNumber) {
            currentNumber++;
          }
          statsNumber.innerText = currentNumber;

          if (currentNumber === finalNumber) {
            clearInterval(incrementNumber);
          }
        }, 1);

        observer.unobserve(entry.target);
      }
    });
  });

  statsItems.forEach((item) => {
    observer.observe(item);
  });
}

animateStats();

const text = "GreenGoods."; // Your desired typing text
const typingSpeed = 500; // Typing speed (in milliseconds)
const cursor = document.getElementById("cursor");
const typingText = document.getElementById("typing-text");

let charIndex = 0;

function typeText() {
  if (charIndex < text.length) {
    const currentChar = text.charAt(charIndex);
    const spanElement = document.createElement("span");
    spanElement.textContent = currentChar;
    if (currentChar === currentChar.toUpperCase() && currentChar !== ".") {
      console.log(currentChar);
      spanElement.classList.add("capital-letter");
    }
    typingText.appendChild(spanElement);
    charIndex++;
    setTimeout(typeText, typingSpeed);
  } else {
    cursor.style.display = "none"; // Hide cursor when typing is done
    sleep(20).then(() => {
      charIndex = 0;
      typingText.innerHTML = ""; // Clear the content inside typingText
      // Start the typing animation again
      setTimeout(typeText, typingSpeed);
    });
  }
}

typeText();



var productimg = document.getElementById("productimg");
var smallimg = document.getElementsByClassName("smallimg");
smallimg[0].onclick = function () {
  productimg.src = smallimg[0].src;
};
smallimg[1].onclick = function () {
  productimg.src = smallimg[1].src;
};
smallimg[2].onclick = function () {
  productimg.src = smallimg[2].src;
};
smallimg[3].onclick = function () {
  productimg.src = smallimg[3].src;
};

let count = 1;

function increaseQuantity() {
  count++;
  updateQuantityDisplay();
}

function decreaseQuantity() {
  if (count > 1) {
    count--;
    updateQuantityDisplay();
  }
}

function updateQuantityDisplay() {
  const quantityDisplay = document.getElementById("quantity-display");
  quantityDisplay.value = count;
}

const tabs = document.querySelectorAll(".tab_btn");
const all_content = document.querySelectorAll(".content");

tabs.forEach((tab, index) => {
  tab.addEventListener("click", (e) => {
    tabs.forEach((tab) => {
      tab.classList.remove("active");
    });
    tab.classList.add("active");

    var line = document.querySelector(".line");
    line.style.width = e.target.offsetWidth + "px";
    line.style.left = e.target.offsetLeft + "px";
    all_content.forEach((content) => {
      content.classList.remove("active");
    });
    all_content[index].classList.add("active");
  });
});

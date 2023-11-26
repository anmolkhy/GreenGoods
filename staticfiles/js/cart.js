//product list from products
const cartItemsEl = document.querySelector("#cart")
const subtotalEl = document.querySelector(".tot")
const subtotalEl2 = document.querySelector(".tot2")
//cart array
let cart = [];

//buttons
var incrementButton = document.getElementsByClassName('inc');
var decrementButton = document.getElementsByClassName('dec');
for (var i = 0; i < incrementButton.length; i++) {
    var button = incrementButton[i];
    button.addEventListener('click', function (event) {
        var buttonClicked = event.target;
        var input = buttonClicked.parentElement.children[1];
        var inputValue = input.value;
        var newValue = parseInt(inputValue) + 1;
        input.value = newValue;

    })
}
for (var i = 0; i < decrementButton.length; i++) {
    var button = decrementButton[i];
    button.addEventListener('click', function (event) {
        var buttonClicked = event.target;
        var input = buttonClicked.parentElement.children[1];
        var inputValue = input.value;
        if (inputValue > 1) {
            var newValue = parseInt(inputValue) - 1;
            input.value = newValue;
        }
    })
}

//ADD TO CART
function addtoCart(id) {
    //take from products.js
    //add a property numberofunits in product.js
    if (cart.some((item) => item.id === id)) {
        changeNumberOfunits("plus", id);
    }
    else {
        const item = products.find((product) => product.id === id);
        cart.push({
            ...item,
            numberofunits: 1,
        });
    }

    updateCart();
}

//update cart
function updateCart() {
    renderCartItems();
    renderSubtotal();
}

function renderCartItems() {
    cart.forEach((item) => {
        cartItemsEl.innerHTML += ''
    });
}

function changeNumberOfunits(action, id) {
    cart * cart.map((item) => {
        let numberofUnits = item.numberofunits;
        if (item.id === id) {
            if (action === "minus" && numberofUnits > 1) {
                numberofUnits--;
            } else if (action === "plus" && numberofUnits < item.inStock) {
                numberofUnits++;
            }
        }
        return {
            ...item,
            numberofUnits,
        };
    });
}


//remove item from cart



var incButton = document.getElementsByClassName("inc");
var decButton = document.getElementsByClassName("dec");
for (var i = 0; i < incButton.length; i++) {
  var button = incButton[i];
  button.addEventListener("click", function (event) {
    var sum = 0;
    for(var j=5;j<10;j++){
        var price = parseInt(document.getElementById("price"+j).innerHTML.replace("Rs.", "").trim());
        var qty = parseInt(document.getElementById("product-quantity"+j).value);
        console.log(price);
        console.log(qty);
        var total = document.getElementById("total"+j);
        total.innerHTML = "Rs." + (price * qty);
        sum = sum + price * qty;
        
    }
    var tot1 = document.getElementById("tot21");
    tot1.innerHTML = "Rs. " + sum;   
    var tot2 = document.getElementById("tot22");
    tot2.innerHTML = "Rs. " + sum;
  });
}
for (var i = 0; i < decButton.length; i++) {
  var button = decButton[i];
  button.addEventListener("click", function (event) {
    var sum = 0;
    for (var j = 5; j < 10; j++) {
      var price = parseInt(
        document
          .getElementById("price" + j)
          .innerHTML.replace("Rs.", "")
          .trim()
      );
      var qty = parseInt(document.getElementById("product-quantity" + j).value);
      console.log(price);
      console.log(qty);
      var total = document.getElementById("total" + j);
      total.innerHTML = "Rs." + price * qty;
      sum = sum + price * qty;
    }
    var tot1 = document.getElementById("tot21");
    tot1.innerHTML = "Rs. " + sum;
    var tot2 = document.getElementById("tot22");
    tot2.innerHTML = "Rs. " + sum;
  });
}


var price1 = parseInt(document.getElementById("price1").innerHTML.replace("Rs.", "").trim());
var price2 = parseInt(document.getElementById("price2").innerHTML.replace("Rs.", "").trim());
var qty1 = parseInt(document.getElementById("product-quantity1").value);
console.log(price1);
console.log(price2);
console.log(qty1);
var total1 = document.getElementById("total1");
total1.innerHTML = "Rs." + (price1 * qty1);




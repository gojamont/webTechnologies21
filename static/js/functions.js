
function getCart() {
    const cart = localStorage.getItem("cart");
    return cart ? JSON.parse(cart) : [];
}

function saveCart(cart) {
    localStorage.setItem("cart", JSON.stringify(cart));
}


// function for registering the user
function registerUser(e) {
    e.preventDefault();

    const data_form = e.target;
    const username = data_form.username.value;
    const password = data_form.password.value;
    const first_name = data_form.first_name.value;
    const last_name = data_form.last_name.value;
    const email = data_form.email.value;

    const csrfToken = data_form.querySelector('[name=csrfmiddlewaretoken]').value;
    
    const error_message = document.querySelector('.error-message');

    error_message.textContent = '';
    error_message.style.display = 'none';

    const data = {
        username: username, 
        password: password, 
        first_name: first_name,
        last_name: last_name, 
        email: email
    }

    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json', 
            'X-CSRFToken' : csrfToken
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => {

            // showing alert when user is registered successfully
            if (data.success) {
                window.location.href = '/login';
            }
            else {
                error_message.textContent = data.message;
                error_message.style.display = 'block';
            }
    })
    .catch(error => console.error('Error', error));
}

// function for logging in the user
function loginUser(e) {
    e.preventDefault();

    const form = e.target;
    const username = form.username.value;
    const password = form.password.value;

    const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value;
    const error_message = document.querySelector('.error-message');

    error_message.textContent = '';
    error_message.style.display = 'none';


    const user_data = {
        username: username, 
        password: password
    }

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json', 
            'X-CSRFToken' : csrfToken
        },
        body: JSON.stringify(user_data)
    })
        .then(response => response.json())
        .then(user_data => {

            // showing alert when user is registered successfully
            if (user_data.success) {
                window.location.href = '/';
            }
            else {
                error_message.textContent = data.message;
                error_message.style.display = 'block';
            }
    })
    .catch(error => console.error('Error', error));

 }

document.addEventListener("DOMContentLoaded", function(){})

// event listener for the sort by price button in catalogue.html
document.addEventListener("DOMContentLoaded", function () {
    const sortBtn = document.getElementById("sortPriceBtn");
    const container = document.querySelector(".ProductsContainer");

    let ascending = true; // toggle

    if (sortBtn) {
        sortBtn.addEventListener("click", () => {
            const cards = Array.from(container.querySelectorAll(".ProductCard"));

            cards.sort((a, b) => {
                const priceA = parseFloat(a.getAttribute("data-price"));
                const priceB = parseFloat(b.getAttribute("data-price"));
                return ascending ? priceA - priceB : priceB - a.priceB;
            });

            // Re-append in new order
            cards.forEach(card => container.appendChild(card));

            // Toggle direction
            ascending = !ascending;
            sortBtn.textContent = ascending ? "Order By Price ↑" : "Order By Price ↓";
        });
    }
});

document.addEventListener("DOMContentLoaded", function () {
    menuIcon = document.getElementById("menu");
    overlay = document.getElementById("overlay");
    cross = document.getElementById("cross");

    menuIcon.addEventListener("click", showMenu);
    overlay.addEventListener("click", hideMenu);
    cross.addEventListener("click", hideMenu);
});

function showMenu () {
    let sideMenu = document.getElementById("side-menu");
    let overlay = document.getElementById("overlay");

    sideMenu.classList.remove("hidden");
    overlay.classList.remove("hidden");
}

function hideMenu () {
    let sideMenu = document.getElementById("side-menu");
    let overlay = document.getElementById("overlay");

    sideMenu.classList.add("hidden");
    overlay.classList.add("hidden");
}
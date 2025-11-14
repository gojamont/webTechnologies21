
function getCart() {
    const cart = localStorage.getItem("cart");
    return cart ? JSON.parse(cart) : [];
}

function saveCart(cart) {
    localStorage.setItem("cart", JSON.stringify(cart));
}


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
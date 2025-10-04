
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
                return ascending ? priceA - priceB : priceB - priceA;
            });

            // Re-append in new order
            cards.forEach(card => container.appendChild(card));

            // Toggle direction
            ascending = !ascending;
            sortBtn.textContent = ascending ? "Order By Price ↑" : "Order By Price ↓";
        });
    }
});

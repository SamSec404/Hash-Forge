document.addEventListener("DOMContentLoaded", () => {

    const searchInput = document.getElementById("history-search");

    if (!searchInput) return;

    searchInput.addEventListener("keyup", function () {

        const filter = this.value.toLowerCase();

        const items = document.querySelectorAll(".history-item");

        items.forEach(item => {

            const text = item.innerText.toLowerCase();

            if (text.includes(filter)) {

                item.style.display = "";

            } else {

                item.style.display = "none";

            }

        });

    });

});
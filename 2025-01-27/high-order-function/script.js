import { foodData } from "./data.js";

const foodList = document.getElementById("food-list");
const uniqueFood = [...new Set(foodData.map((food) => food.name))];

uniqueFood.forEach((name) => {
    const listFoodItem = document.createElement("li");
    listFoodItem.innerHTML = `<a href="#" data-name="${name}">${name}</a>`;
    foodList.appendChild(listFoodItem);
});

document.querySelectorAll('#food-list a').forEach((link) => {
    link.addEventListener('click', function (e) {
        e.preventDefault();
        const name = this.dataset.name;
        showFoodDetail(name);
    });
});

function showFoodDetail(name) {
    const foodDetail = document.getElementById("food-detail");
    const foodName = document.getElementById("food-name");
    const foodDataTable = document.getElementById("food-data");
    const totalCost = document.getElementById("total-cost");

    const foodEntry = foodData.filter((food) => food.name === name);

    foodName.textContent = `${name}'s Details`;
    
    foodDataTable.innerHTML = foodEntry
        .map((entry) => {
            const totalValue = entry.quantity * entry.price; 
            return `<tr>
                <td>${entry.date}</td>
                <td>${entry.quantity}</td>
                <td>${entry.price}</td>
                <td>${totalValue}</td>
            </tr>`;
        })
        .join("");

    const grandTotal = foodEntry.reduce(
        (sum, entry) => sum + (entry.quantity * entry.price),
        0
    );
    totalCost.textContent = `Total Cost: ${grandTotal}`;

    document.querySelector("#food-list").style.display = "none";
    foodDetail.style.display = "block";
}

    document.getElementById("back-button").addEventListener("click", () => {
    document.getElementById("food-detail").style.display = "none";
    document.querySelector("#food-list").style.display = "block";
});

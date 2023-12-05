// ^ map, filter, find, forEach

// * map
const nums = [2, 2, 3, 5];
const squares = nums.map((x) => x * x);
console.log(squares);

// * filter
const product = [
    { id: 1, name: "Apple", price: 10, color: "red" },
    { id: 2, name: "Samsung", price: 20, color: "white" },
    { id: 3, name: "Motorola", price: 15, color: "black" },
    { id: 4, name: "Sony", price: 30, color: "black" }
];

const result = product.filter((item) => item.color == "black");
console.log(result);

// * find
console.log(product.find((item) => item.color == "black"));

const productContainer = document.getElementById("product-container");

// * forEach
const result2 = product.forEach((product) => {
    console.log(product);
    const h1 = document.createElement("h1");
    h1.innerText = product.name;
    productContainer.appendChild(h1);
});

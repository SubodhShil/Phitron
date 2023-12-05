// alert("Hi, This is an alert!!");

let allHeaderTags = document.getElementsByTagName("h1");
console.log(allHeaderTags);

// ^ To select a unique or single tag
let allH2Tags = document.getElementById("h2-tag");
console.log(allH2Tags);
allH2Tags.style.color = "orangered";
allH2Tags.style.textDecoration = "underline";
allH2Tags.style.textDecorationColor = "green";

// ^ get the text from a tag
console.log(`The inner text is: ${allH2Tags.innerText}`);

// ^ To select multiple tags
let classTags = document.getElementsByClassName("header");
console.log(classTags);
console.log(`First selected: ${classTags[0]}`);

const imageSelect = document.getElementById("img");
console.log(`Image src: ${imageSelect.getAttribute("src")}`);
imageSelect.setAttribute("alt", "Picture");
imageSelect.setAttribute(
    "src",
    "https://images.unsplash.com/photo-1682686581776-b6ebee7c150e?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
);
imageSelect.setAttribute("width", "700px");

// * set class attribute
imageSelect.classList.add("DOM-class");
console.log(imageSelect);

// ^ inner html
const parentDiv = document.getElementById("parent-div");
console.log(parentDiv);

const testDiv = document.getElementsByClassName("test");
console.log(`The test div`);

// ^ child node
console.log(testDiv[0].childNodes[1]);
// ^ parent node
console.log(testDiv[0].childNodes[1].parentNode);
console.log(testDiv[0].childNodes[1].parentNode.parentNode);
console.log(testDiv[0].childNodes[1].parentNode.parentNode.parentNode);

// * Create element
let p = document.createElement("p");
p.innerText = "Created by JS";
parentDiv.appendChild(p);

// ^ input tag value
const inputTagSelect = document.getElementsByTagName("input");
console.log("Input tag: ", inputTagSelect);

// ^ Even listener
let buttonEvent = document.getElementById("submit-btn");
buttonEvent.addEventListener("click", function (e) {
    console.log("button is clicked!!");
    console.log(`Value of input tag is: ${inputTagSelect[0].value}`);
});

// ^ Blur event
/* document.getElementById("input").addEventListener("blur", function (e) {
    console.log(e.target.value);
});
 */

function inputChange(e) {
    console.log(e);
}

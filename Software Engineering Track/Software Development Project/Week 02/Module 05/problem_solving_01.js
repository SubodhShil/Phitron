const readline = require("readline");

const userInput = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// ^ Q1: Sort numbers
let numbers = [2, 8, 10, 4, -3, 55, 199];
numbers.sort((a, b) => a - b);
console.log(numbers);

//^ Q2: Find the largest string
let friends = ["Kira", "Irasan", "Roktim", "Pulkit", "Doraemonkey"];
let largestStr = friends[0];

for (let i = 1; i < friends.length; ++i) {
    largestStr = largestStr.length < friends[i].length ? friends[i] : largestStr;
}

console.log(largestStr);

// ^ Q3: If a number is even or odd
userInput.question("Enter a number: ", (num) => {
    if (num & 1) console.log(`${num} is odd\n`);
    else console.log(`${num} is even`);

    userInput.close();
});

console.log("Hello JavaScript World!!!");
console.log(2 * 12 * 1.7);

// Check type
var a = 5324;
let b = false;
let c = "Human";
let d = {
    name: "Somebody"
};

console.log(typeof a, typeof b, typeof c, typeof d);

// Fractional to decimal
var num1 = 70.55;
var num2 = 33;
console.log(parseInt(num1 + num2));

// Add to 'string' formated number and get a number
var strNum1 = "100";
var strNum2 = "50.5";
console.log(parseInt(strNum1) + parseInt(strNum2));

// JS Objects
var person = {
    hands: 2,
    eyes: 2,
    nose: 1,
    legs: 2,
    dil: 1
};

console.log(Object.keys(person));
console.log(Object.values(person));
console.log(Object.entries(person));

// JS Array
var hariNam = ["Hare", "Krishna", "Hare", "Rama"];
console.log(hariNam[hariNam.length - 1]);

let games = ["GTA 5", "Call of Duty", "Battlefield 5"];

games.unshift("Rise of The Tomb Raider");
console.log(games);

games.shift();
console.log(games);

let newGames = games.concat("Wolfenstine");
console.log(newGames);

newGames.reverse();

console.log(newGames.join(" + "));

console.log(newGames.slice(0, 2));

console.log(newGames.indexOf("GTA 5"));

console.log(newGames.includes("GTA 5"));

// * For Loops
for (let i = 0; i < newGames.length - 1; ++i) console.log(newGames[i]);


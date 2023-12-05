const num = [1, 2, 33, 55];
console.log(...num);

const newArr = [-1, 0, ...num];
console.log(newArr);

// Array Destructuring
const [first, second, third] = newArr;
console.log(first, second, third);

// Find maximum
console.log(Math.max(...num));

// Arrow function
const power = (x) => {
    return Math.pow(x, x);
};
console.log(power(3));

// for one liner
const addItself = (x) => x + x;
console.log(addItself(10));

// Object Destructuring
const myself = {
    name: "Subodh",
    age: 24,
    hasJob: "Jobless",
    github: "yes"
};

const { name, github, age, hasJob } = myself;
console.log(name, github, age, hasJob);

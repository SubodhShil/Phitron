fetch("https://fakestoreapi.com/products/1")
    .then((res) => res.json)
    .then((data) => {
        console.log(data);
    })
    .catch((err) => {
        console.log(`Got some problem ${err}`);
    });

const getData = new Promise(function (resolve, reject) {
    return resolve(20);
});

// Fetching using async, await
const loadData = async () => {
    try {
        const response = await fetch("https://fakestoreapi.com/products/1");
        // console.log(response.json());
        const data = await response.json();
        console.log(data);
    } catch {
        (err) => console.log(err);
    }
};

loadData();

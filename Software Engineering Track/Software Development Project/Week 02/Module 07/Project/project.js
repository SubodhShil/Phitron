const loadData = () => {
    const searchText = document.getElementById("searchBox").value;
    const searchTerm = searchText.split(" ")[0];
    console.log(searchText, searchTerm);

    if (searchText == "") {
        console.log("No text input");
        return;
    }

    // Clear the input field
    document.getElementById("searchBox").value = "";
    const dynamicLink = `https://www.themealdb.com/api/json/v1/1/search.php?s=${searchTerm}`;
    console.log(searchText, dynamicLink);

    fetch(dynamicLink)
        .then((res) => res.json(dynamicLink))
        .then((data) => displayData(data.meals));
};

const displayData = (data) => {
    document.getElementById(
        "text-result"
    ).innerText = `Total result: ${data.length}`;

    const mealsContainer = document.getElementById("meals-section");

    data.forEach((meal) => {
        console.log(meal);
        const card = document.createElement("div");
        card.innerHTML = `
        <div class="border border-2 p-2 m-2">        
            <h2 class="text-wrap text-decoration-underline">${meal.strMeal}</h2>
            <img src="${meal.strMealThumb}" class="w-100 w-lg-25" alt=""> 

            <!-- Button trigger modal -->
            <button type="button" class="btn btn-primary mt-3" data-bs-toggle="modal" data-bs-target="#exampleModal">
            Read More..
            </button>

            <!-- Modal -->
            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    ${meal.strInstructions}
                </div>
                <div class="modal-footer">
                    <button type="button" class="border-0 rounded-2 bg-danger text-white fw-bold" data-bs-dismiss="modal">Close</button>
                    <button class="border-0 rounded-2 bg-success"><a class="text-decoration-none text-white fw-bold" target="_blank" href="${meal.strYoutube}">See Video</a></button>
                </div>
                </div>
            </div>
            </div>
        </div>
        `;

        mealsContainer.appendChild(card);
    });
};

const resultSection = document.getElementById("result-section");
const currentPage = document.getElementById("current-page");

// * All category
const allCategory = document.getElementById("all-category");
const allCategoryAPI = `https://openapi.programming-hero.com/api/videos/category/1000`;

// * Music category
const musicCategory = document.getElementById("music-category");
const musicCategoryAPI = `https://openapi.programming-hero.com/api/videos/category/1001`;

// * Comedy category
const comedyCategory = document.getElementById("comedy-category");
const comedyCategoryAPI = `https://openapi.programming-hero.com/api/videos/category/1003`;

// * Drawing category
const drawingCategory = document.getElementById("drawing-category");

const fetchinData = (url) => {
    fetch(url)
        .then((response) => response.json())
        .then((data) => handleData(data));
};

const handleData = (e) => {
    clearResults();
    e.data.forEach((element) => {
        const card = document.createElement("div");
        const postedHistory = element.others.posted_date;
        const postedHour = Math.floor(postedHistory / 3600);
        const postedMinute = Math.floor((postedHistory % 3600) / 60);

        card.innerHTML = `
        <div class="" style="cursor:pointer"> 

            <div id="thumbnail-image" class="position-relative">
                ${
                    postedHistory > 0
                        ? `<p style="font-size:12px" class="bg-warning-subtle position-absolute bottom-0 p-1 end-0 me-2 rounded-2">${postedHour} hours ${postedMinute} minutes ago</p>`
                        : ""
                }
            </div>

            <br>

            <div class="d-flex gap-2 mt-1">
                <div>
                    <img src="${
                        element.authors[0].profile_picture
                    }" alt="" width="40px" height="40px" class="rounded rounded-circle">
                </div>
                <div>
                    <h6 class="fw-bold">${element.title}</h6>
                    <h6 style="color:gray">${element.authors[0].profile_name} ${
            element.authors[0].verified == true
                ? `<i class="text-primary bi-patch-check-fill"></i>`
                : ""
        }  </h6>
                    <p style="color:gray">${element.others.views} views</p>
                </div>
            </div>
        </div>
        `;
        const thumbnailImage = card.querySelector("#thumbnail-image");
        thumbnailImage.style.backgroundImage = `url('${element.thumbnail}')`;
        thumbnailImage.style.backgroundSize = "cover";
        thumbnailImage.style.width = "420px";
        thumbnailImage.style.height = "250px";
        thumbnailImage.classList.add("rounded", "rounded-2");

        resultSection.appendChild(card);
    });
};

const clearResults = () => {
    resultSection.innerHTML = "";
};

// ~ Default: all category
fetchinData(allCategoryAPI);

allCategory.addEventListener("click", () => fetchinData(allCategoryAPI));

musicCategory.addEventListener("click", () => fetchinData(musicCategoryAPI));

comedyCategory.addEventListener("click", () => fetchinData(comedyCategoryAPI));

drawingCategory.addEventListener("click", () => handleDrawingCategory());

const handleDrawingCategory = () => {
    clearResults();
    const path = "./Media/Icon.png";
    const noContent = document.createElement("div");
    noContent.innerHTML = `
        <div class="d-flex flex-column justify-content-center">
            <div class="m-auto">
                <img src="${path}" alt="" width="120px" height="120px" class="">
            </div>
            <h1 style="font-family: 'Montserrat'" class="fw-bold text-wrap text-center">Oops!! Sorry, There is no content here</h1>
        </div>
    `;

    resultSection.appendChild(noContent);
};
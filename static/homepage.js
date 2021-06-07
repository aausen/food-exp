'use strict';

// $.get('https://shelf-life-api.herokuapp.com/guides/18794', (res) => {
//     let foodInfo = res;
//     console.log(foodInfo);
// })

// const foodItem = document.getElementById('foodItem');
// const searchBar = document.getElementById('searchBar');

// searchBar.addEventListener('keyup', (e) => {
//     console.log(e);
// });

// const loadFood = $.get('https://shelf-life-api.herokuapp.com/search?q=%7Bsearch_query%7D', (res) =>{
//     let foodInfo = res;
//     displayFood(foodInfo);
//     console.log(foodInfo);
// })

// const displayFood = (food) =>{
//     const htmlString = food
//     .map((food) => {
//         return `
//         <li class="food">
//             <h2>${food.name}</h2>
//             <p>Location: ${food.location}</p>
//             <p>Shelf life: ${food.expiration}</p>
//             <p>Tips: ${food.tips}</p>
//             </li>
//             `;
//     })
//     foodItem.innerHTML = htmlString;
// };

// loadFood();
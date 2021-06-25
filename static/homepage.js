'use strict';

let td = document.querySelectorAll('td');
let foodCount = td.length/3;
let i = 2;
const expDateArray = [];
const expDateObjs = [];
while (i < td.length){
    let expDate = td[i].innerHTML;
    expDateObjs.push(td[i]);
    expDateArray.push(expDate);
    i = i + 4;

}

let counter = 0;
for (let dateExp of expDateArray) {
    let timeNow = new Date();
    dateExp = new Date(dateExp);
    if(timeNow >= dateExp){
        expDateObjs[counter].style.color = 'red';
        }
        
        counter ++;
}

// on change handler for .location-filter els
// each .loc-filter has data-location="name of location"
// func that takes in location name and boolean (hide/unhide)
// showRowsByLocation(' Fridge', true) => show all ' Fridge' rows
//                               false => hide
//

// Syntax for adding Bootstrap class to set display: none;
// element.classList.add('d-none');
// To remove class
// element.classList.remove('d-none');

function showRowsByLocation(loc, shouldHidden) {
    const trs = document.querySelectorAll('.food-entry');

    const locRows = [];
    for (const tr of trs) {
        if (getFoodRowLocation(tr).trim() === loc.trim()) {
            locRows.push(tr);
        }
    }

    
    for (const location of locRows) {
        if (shouldHidden) {
            location.classList.add('d-none');
        } else {
            location.classList.remove('d-none');
        }
    }
}

function getFoodRowLocation(trEl) {
    const td = trEl.querySelector('td[data-loc]');
    return td.dataset.loc;
}

// function showAll() {
//     let x = document.getElementById("myDiv");
//     if (x.style.display === "none"){
//         x.style.display = "block";
//     } else {
//         x.style.display = "none";
//     }
// }

// function showFridge() {
//     let tdata = document.querySelectorAll('td');
//     let x = 1
//     const locArray = [];
//     while (x < tdata.length){
//         let loc = tdata[x].innerHTML;
//         locArray.push(loc);
//         x = x + 4;
//     };

//     let count = 1;
//     let tr = document.querySelectorAll('tr')
//     // console.log(tr);
//     for(let locc of locArray){
//         // console.log("**")
//         // console.log(tr[count]);
//         if(locc !== " Refrigerator"){ // check whether locc is inside one of the selected locations
//             let y = tr[count]
//             if(y.style.visibility === 'collapse'){
//                 y.style.visibility = 'visible';
//             } else{
//                 y.style.visibility = 'collapse';
//             }
//         }
//         count ++;
//     }
// };

// function showFreezer() {
//     let tdata = document.querySelectorAll('td');
//     let x = 1
//     const locArray = [];
//     while (x < tdata.length){
//         let loc = tdata[x].innerHTML;
//         locArray.push(loc);
//         x = x + 4;
//     };

//     let count = 1;
//     let tr = document.querySelectorAll('tr')
//     // console.log(tr);
//     for(let locc of locArray){
//         // console.log("**")
//         // console.log(tr[count]);
//         if(locc !== " Freezer"){ 
//             let y = tr[count]
//             if(y.style.visibility === 'collapse'){
//                 y.style.visibility = 'visible';
//             } else{
//                 y.style.visibility = 'collapse';
//             }
//         }
//         count ++;
//     }
// };

// function showPantry() {
//     let tdata = document.querySelectorAll('td');
//     let x = 1
//     const locArray = [];
//     while (x < tdata.length){
//         let loc = tdata[x].innerHTML;
//         locArray.push(loc);
//         x = x + 4;
//     };

//     let count = 1;
//     let tr = document.querySelectorAll('tr')
//     // console.log(tr);
//     for(let locc of locArray){
//         // console.log("**")
//         // console.log(tr[count]);
//         if(locc !== " Pantry"){ 
//             let y = tr[count]
//             if(y.style.visibility === 'collapse'){
//                 y.style.visibility = 'visible';
//             } else{
//                 y.style.visibility = 'collapse';
//             }
//         }
//         count ++;
//     }
// };

function filterByLocation(){
    // Get all the buttons from the html
    const buttons = Array.from(document.querySelectorAll('input.btn-check'));
    // Get list of which buttons are currently checked
    let selectedButtons = buttons.filter(button => button.checked);
    // Create a list of the string locations that are checked
    let activeLocations = selectedButtons.map(button => {return button.getAttribute('data-location')})
   
    // Get each row from food table
    const rows = document.querySelectorAll('td');
    // Set counting var for traversing the table
    let x = 1;
    // Create an array to store all locations from table
    const locArray = [];
    // For the whole table, get the string locaiton for each food
    while (x < rows.length){
        let loc = rows[x].innerHTML;
        locArray.push(loc);
        x = x + 4;
    }
    console.log(locArray)
    // Create counter
    let count = 1;
    // Select the table rows
    let tr = document.querySelectorAll('tr')
    // For each locaiton in the location array
    for(let loc of locArray){
        // Variable for each row to select the row
        let y = tr[count];
        console.log(y)
        // If the button array active locations includes the location from the food table
        if(activeLocations.includes(loc)){
            console.log("Visible", loc)
            // Show the foods if the button is checked
            y.style.display = null;
        }else{
            console.log("not visible", loc)
            // Collapes if the button is not checked
            y.style.display = 'none';
        }
    }
    // Increment to get to the next row
    count ++;
    
};


// // Every time you click a button
// function filterByLocation(){
//     buttons = document.querySelectorAll()
//     selectedButtons = buttons.filter(function (button){
//       button.checked
//     })
//     activeLocations = selectedButtons.map(function (button){
//       button.datasets['locations']
//     })
  
//     const rows = Array.from(document.querySelectorAll('tr'));
//     for loop -> rows.each(function (button){
//       if row.location is in any activeLocations
//         row.show
//       else
//         row.hide
//       end
//     })
//   }


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

// ____________________ Functions for showing/hiding rows__________________________________//

// Hides the rows in the table that are not checked (called in initializeLocationFilters)
function hideRowsNotInLocations(locs) {
    // Get the table rows
    const trs = document.querySelectorAll('.food-entry');

    // Add the rows that are not in the given list
    const locRows = [];
    for (const tr of trs) {
        if (!locs.includes(getFoodRowLocation(tr).trim())) {
            locRows.push(tr);
        }
    }

    // Hide any row that is in the array
    for (const location of locRows) {
        location.classList.add('d-none');
    }
}

// Shows the rows in the table that are checked (called in initializeLocationFilters)
function showRowsInLocations(locs) {
    // Get the table rows
    const trs = document.querySelectorAll('.food-entry');

    // Add the rows that are inclueded in the given array
    const locRows = [];
    for (const tr of trs) {
        if (locs.includes(getFoodRowLocation(tr).trim())) {
            locRows.push(tr);
        } 
    }

    // Show any row that is in the list
    for (const location of locRows) {
        location.classList.remove('d-none');
    }
}

// Shows all the rows
function showAllRows() {
    // Get all the table rows
    const trs = document.querySelectorAll('.food-entry');

    // Add all the rows to the new array
    const locRows = [];
    for (const tr of trs) {
        locRows.push(tr);
    }

    // Show all the rows
    for (const location of locRows) {
        location.classList.remove("d-none");
    }
}

function getFoodRowLocation(trEl) {
    // Select all the data cells with data-loc (location cells) and return them 
    const td = trEl.querySelector('td[data-loc]');
    return td.dataset.loc;
}

// Return array of location names of filters that are checked
function getActiveLocations() {
    // Get all the buttons
    const locFilters = document.querySelectorAll('.location-filter');

    // Add each button that is checked and add it to array and return the array
    const activeLocations = [];
    for (const locFilter of locFilters) {
        if (locFilter.checked) {
            activeLocations.push(locFilter.dataset.location.trim());
        }
    }
    return activeLocations;
}


// Has on change listener and actually changes the state of the page
function initializeLocationFilters() {
    // Get all the buttons
    const locFilters = document.querySelectorAll('.location-filter');

    // Listen for a change on any of the buttons and get the active location
    for (const locFilter of locFilters) {
        locFilter.addEventListener('change', () => {
            const activeLocations = getActiveLocations();
            
            // If there are no active locations, show all. If there are active locations, show/hide appropriate rows
            if (activeLocations.length == 0){
                showAllRows();
            } else {
                hideRowsNotInLocations(activeLocations);
                showRowsInLocations(activeLocations);
            }
        });
    }
}
initializeLocationFilters();


// each .loc-filter has data-location="name of location"
// func that takes in location name and boolean (hide/unhide)
// showRowsByLocation(' Fridge', true) => show all ' Fridge' rows
//                               false => hide
//

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


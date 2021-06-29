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
        expDateObjs[counter].classList.add("table-danger");
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



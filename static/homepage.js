'use strict';

let td = document.querySelectorAll('td');
let foodCount = td.length/3;
let i = 2;
const expDateArray = []
while (i < td.length){
    let expDate = td[i].innerHTML;
    expDateArray.push(expDate)
    i = i + 3;
    
}

for (let dateExp of expDateArray) {
    // console.log(dateExp);
    let timeNow = new Date();
    dateExp = new Date(dateExp);
    console.log(dateExp);
    // timeNow = timeNow.toDateString();
    console.log(timeNow);
    if(timeNow >= dateExp){
        dateExp.style.color = 'red';
        }
}

    
// console.log(expDateArray);

// console.log(new Date());
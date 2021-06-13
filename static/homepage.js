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
    console.log(dateExp);
    let timeNow = new Date();
    timeNow = timeNow.toString();
    console.log(timeNow);
    if(dateExp == timeNow){
        dateExp.style.color = 'red';
        }
}

    
console.log(expDateArray);

console.log(new Date());
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
    let timeNow = new Date();
    dateExp = new Date(dateExp);
    if(timeNow >= dateExp){
        dateExp = dateExp.toDateSTring();
        while (i < td.length){
            let expDate = td[i].innerHTML;
            if(expDate == dateExp){
                expDate.style.color = 'red';
            }
            i = i + 3;
        }
    }
}


    
// console.log(expDateArray);

// console.log(new Date());
// dateExp.style.color = 'red'
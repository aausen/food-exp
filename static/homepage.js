'use strict';

const expDate = document.getElementById('exp_date').textContent;
    console.log(expDate)
    const timeNow = new Date();
    if(expDate == timeNow){
        expDate.style.color = 'red';
    }

console.log(new Date())
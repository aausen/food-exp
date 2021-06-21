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


function showAll() {
    let x = document.getElementById("myDiv");
    if (x.style.display === "none"){
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function showFridge() {
    let tdata = document.querySelectorAll('td');
    let x = 1
    const locArray = [];
    const locObjs = [];
    while (x < tdata.length){
        let loc = tdata[x].innerHTML;
        locObjs.push(tdata[x]);
        locArray.push(loc);
        x = x + 4;
        // console.log(locArray);
    };

    let count = 0;
    let tr = document.querySelectorAll('tr')
    console.log(tr);
    for (let loc of locArray){
        console.log(loc);
        if(loc !== "Refrigerator"){ 
            if($('tr:has(loc)')){
                tr.style.display = "none";
            }
        }
       
        counter ++;
    }
    
    
}


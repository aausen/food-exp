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
    while (x < tdata.length){
        let loc = tdata[x].innerHTML;
        locArray.push(loc);
        x = x + 4;
    };

    let count = 1;
    let tr = document.querySelectorAll('tr')
    console.log(tr);
    for(let locc of locArray){
        console.log("**")
        console.log(tr[count]);
        if(locc !== " Refrigerator"){ // check whether locc is inside one of the selected locations
            let y = tr[count]
            if(y.style.visibility === 'collapse'){
                y.style.visibility = 'visible';
            } else{
                y.style.visibility = 'collapse';
            }
        }
        count ++;
    }
};

function showFreezer() {
    let tdata = document.querySelectorAll('td');
    let x = 1
    const locArray = [];
    while (x < tdata.length){
        let loc = tdata[x].innerHTML;
        locArray.push(loc);
        x = x + 4;
    };

    let count = 1;
    let tr = document.querySelectorAll('tr')
    console.log(tr);
    for(let locc of locArray){
        console.log("**")
        console.log(tr[count]);
        if(locc !== " Freezer"){ 
            let y = tr[count]
            if(y.style.visibility === 'collapse'){
                y.style.visibility = 'visible';
            } else{
                y.style.visibility = 'collapse';
            }
        }
        count ++;
    }
};

function showPantry() {
    let tdata = document.querySelectorAll('td');
    let x = 1
    const locArray = [];
    while (x < tdata.length){
        let loc = tdata[x].innerHTML;
        locArray.push(loc);
        x = x + 4;
    };

    let count = 1;
    let tr = document.querySelectorAll('tr')
    console.log(tr);
    for(let locc of locArray){
        console.log("**")
        console.log(tr[count]);
        if(locc !== " Pantry"){ 
            let y = tr[count]
            if(y.style.visibility === 'collapse'){
                y.style.visibility = 'visible';
            } else{
                y.style.visibility = 'collapse';
            }
        }
        count ++;
    }
};

function filterByLocation(){
    let buttons = Array.from(document.querySelectorAll('input.btn-check'));
    let selectedButtons = buttons.filter(button => button.checked);
    // let activeLocations = selectedButtons.map()

    let rows = document.querySelectorAll('tr')
    rows.foreach()
}


// // Every time you click a button
// function filterByLocation(){
//     buttons = document.querySelectorAll()
//     selectedButtons = buttons.filter(function (button){
//       button.checked
//     })
//     activeLocations = selectedButtons.map(function (button){
//       button.datasets['locations']
//     })
  
//     rows = document.querySelectorAll('tr')
//     for loop -> rows.each(function (button){
//       if row.location is in any activeLocations
//         row.show
//       else
//         row.hide
//       end
//     })
//   }
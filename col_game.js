// var numsquares = 6;
// var cols = generatrandomcolor(numsquares);
// var resetcolor = document.getElementById('reset');

// var pickcolor = PickColor();
// console.log(pickcolor)
// var colordisplay = document.getElementById('colordisplay')
// var sqaures = document.querySelectorAll(".square");
// var msg = document.querySelector("#message");
// var H1 = document.querySelector('h1');
// var easy = document.querySelector('#easy');
// var hard = document.querySelector('#hard');

// easy.addEventListener('click',function(){
//     numsquares = 3
//     easy.classList.add('selected');
//     hard.classList.remove('selected');
//     cols = generatrandomcolor(numsquares);
//     pickcolor = PickColor();
//     colordisplay.textContent = pickcolor;
//     for (let index = 0; index < sqaures.length; index++) {
//         if (cols[index]) {
//             sqaures[index].style.backgroundColor = cols[index];
//         } else {
//             sqaures[index].style.display = "none";
//         }
//     }
//     H1.style.background = "steelblue";
//     msg.textContent = "";
// });
// hard.addEventListener('click',function(){
//     numsquares = 6;
//     easy.classList.remove('selected');
//     hard.classList.add('selected');
//     cols = generatrandomcolor(numsquares);
//     pickcolor = PickColor();
//     colordisplay.textContent = pickcolor;
//     for (let index = 0; index < sqaures.length; index++) {
//         sqaures[index].style.backgroundColor = cols[index];
//         sqaures[index].style.display = "block";
//     }
//     H1.style.background = "steelblue";
//     msg.textContent = "";
// });
// colordisplay.textContent = pickcolor;

// for (var index = 0; index < sqaures.length; index++) {
//     sqaures[index].style.backgroundColor = cols[index];

//     sqaures[index].addEventListener('click',function(){
//         clickcol = this.style.backgroundColor;

//         if(pickcolor === clickcol){
//             msg.textContent = "Correct!";
//             resetcolor.textContent = "Play Again?"
//             changecolor(clickcol);
//             H1.style.backgroundColor = pickcolor;
//         } else {
//             this.style.backgroundColor = "#191919";
//             msg.textContent = "Try Again!";
//         }

//     });
// }
// resetcolor.addEventListener('click',function(){
//     cols = generatrandomcolor(numsquares);
//     pickcolor = PickColor();
//     resetcolor.textContent = "NEW COLORS"
//     colordisplay.textContent = pickcolor;
//     for (let index = 0; index < sqaures.length; index++) {
//             sqaures[index].style.backgroundColor = cols[index];
//     }
//     H1.style.background = "steelblue";
//     msg.textContent = ""
// });

// function changecolor(color) {
//     for (let i = 0; i < sqaures.length; i++) {
//         sqaures[i].style.backgroundColor = clickcol; 
//     }

// }

// function PickColor() {
//     var rand = Math.floor(Math.random() * cols.length);
//     return cols[rand];
// }

// function generatrandomcolor(num){
//     var a = [];
//     for (let i = 0; i < num; i++) {
//         a.push(randomcolor());
//     }
//     return a;
// }

// function randomcolor() {
//     var r = Math.floor(Math.random() * 256);
//     var g = Math.floor(Math.random() * 256);
//     var b = Math.floor(Math.random() * 256);
//     return "rgb(" + r + ", " + g + ", " + b + ")";
// }
// Refracted Code ==========>>
var numsquares = 6;
var cols = generatrandomcolor(numsquares);
var resetcolor = document.getElementById('reset');
var pickcolor = PickColor();
var colordisplay = document.getElementById('colordisplay')
var sqaures = document.querySelectorAll(".square");
var msg = document.querySelector("#message");
var H1 = document.querySelector('h1');
var modebtns = document.querySelectorAll('.mode');

colordisplay.textContent = pickcolor;
for (var index = 0; index < sqaures.length; index++) {
    sqaures[index].style.backgroundColor = cols[index];

    sqaures[index].addEventListener('click', function () {
        clickcol = this.style.backgroundColor;

        if (pickcolor === clickcol) {
            msg.textContent = "Correct!";
            resetcolor.textContent = "Play Again?"
            changecolor(clickcol);
            H1.style.backgroundColor = pickcolor;
        } else {
            this.style.backgroundColor = "#191919";
            msg.textContent = "Try Again!";
        }

    });
}
for (let index = 0; index < modebtns.length; index++) {
    modebtns[index].addEventListener('click', function () {
        modebtns[0].classList.remove('selected');
        modebtns[1].classList.remove('selected');
        this.classList.add('selected');
        this.textContent === "EASY" ? numsquares = 3 : numsquares = 6;
        Reset();
    })

}

function Reset() {
    cols = generatrandomcolor(numsquares);
    pickcolor = PickColor();
    resetcolor.textContent = "NEW COLORS"
    colordisplay.textContent = pickcolor;
    for (let index = 0; index < sqaures.length; index++) {
        if (cols[index]) {
            sqaures[index].style.backgroundColor = cols[index];
            sqaures[index].style.display = 'block';
        } else {
            sqaures[index].style.display = 'none';
        }
    }
    H1.style.background = "steelblue";
    msg.textContent = "";
}

resetcolor.addEventListener('click', function () {
    Reset();
});

function changecolor(color) {
    for (let i = 0; i < sqaures.length; i++) {
        sqaures[i].style.backgroundColor = clickcol;
    }

}

function PickColor() {
    var rand = Math.floor(Math.random() * cols.length);
    return cols[rand];
}

function generatrandomcolor(num) {
    var a = [];
    for (let i = 0; i < num; i++) {
        a.push(randomcolor());
    }
    return a;
}

function randomcolor() {
    var r = Math.floor(Math.random() * 256);
    var g = Math.floor(Math.random() * 256);
    var b = Math.floor(Math.random() * 256);
    return "rgb(" + r + ", " + g + ", " + b + ")";
}
var today = new Date();
var mand = today.getMonth();
function maand(maand) {
    document.getElementById((24 + maand) % 12).innerHTML = "Januari";
    document.getElementById((23 + maand) % 12).innerHTML = "Februari";
    document.getElementById((22 + maand) % 12).innerHTML = "Maart";
    document.getElementById((21 + maand) % 12).innerHTML = "April";
    document.getElementById((20 + maand) % 12).innerHTML = "Mei";
    document.getElementById((19 + maand) % 12).innerHTML = "Juni";
    document.getElementById((18 + maand) % 12).innerHTML = "Juli";
    document.getElementById((17 + maand) % 12).innerHTML = "Augustus";
    document.getElementById((16 + maand) % 12).innerHTML = "September";
    document.getElementById((15 + maand) % 12).innerHTML = "Oktober";
    document.getElementById((14 + maand) % 12).innerHTML = "November";
    document.getElementById((13 + maand) % 12).innerHTML = "December";
}
maand(mand);
function flap(i){
    if (document.getElementById(i + "transacties").style.display == "flex"){
        document.getElementById(i + "transacties").style.display = "none";
    }
    else {
        document.getElementById(i + "transacties").style.display = "flex";
    }
}
document.getElementById(0).onclick = function() {
    flap(0);
};
document.getElementById(1).onclick = function() {
    flap(1);
};
document.getElementById(2).onclick = function() {
    flap(2);
};
document.getElementById(3).onclick = function() {
    flap(3);
};
document.getElementById(4).onclick = function() {
    flap(4);
};
document.getElementById(5).onclick = function() {
    flap(5);
};
document.getElementById(6).onclick = function() {
    flap(6);
};
document.getElementById(7).onclick = function() {
    flap(7);
};
document.getElementById(8).onclick = function() {
    flap(8);
};
document.getElementById(9).onclick = function() {
    flap(9);
};
document.getElementById(10).onclick = function() {
    flap(10);
};
document.getElementById(11).onclick = function() {
    flap(11);
};
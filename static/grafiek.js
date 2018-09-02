// load packages
google.charts.load("current", {packages: ['corechart']});

document.getElementById("title").onclick =function(){
    if (document.getElementById("test").innerHTML == ""){
        drawChart();
    }
    else if (document.getElementById("test").style.display == "none"){
        document.getElementById("test").style.display = "block";
    }
    else {
        document.getElementById("test").style.display = "none";
    }
};
document.getElementById("inkomst").onclick =function(){
    if (document.getElementById("inkomst-g").innerHTML == ""){
        drawCat();
    }
    else if (document.getElementById("inkomst-g").style.display == "none"){
        document.getElementById("inkomst-g").style.display = "block";
    }
    else {
        document.getElementById("inkomst-g").style.display = "none";
    }
};
document.getElementById("cash").onclick =function(){
    if (document.getElementById("cash-graph").innerHTML == ""){
        drawCash();
    }
    else if (document.getElementById("cash-graph").style.display == "none"){
        document.getElementById("cash-graph").style.display = "block";
    }
    else {
        document.getElementById("cash-graph").style.display = "none";
    }
};
document.getElementById("ink").onclick =function(){
    if (document.getElementById("ink-graph").innerHTML == ""){
        drawInk();
    }
    else if (document.getElementById("ink-graph").style.display == "none"){
        document.getElementById("ink-graph").style.display = "block";
    }
    else {
        document.getElementById("ink-graph").style.display = "none";
    }
};

var today = new Date();
var maand = today.getMonth();
var year = today.getFullYear();

function drawChart(){
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Categorie');
    data.addColumn('number', 'bedrag');
    data.addRows([
        ['winkel', parseFloat(winkel)],
        ['restaurant', parseFloat(restaurant)],
        ['openbaarVervoer', parseFloat(openbaarVervoer)],
        ['auto', parseFloat(auto)],
        ['verzekering', parseFloat(verzekering)],
        ['dokters', parseFloat(dokters)],
        ['kleren', parseFloat(kleren)],
        ['abonnementen', parseFloat(abonnementen)],
        ['diensten', parseFloat(diensten)],
        ['elektronica', parseFloat(elektronica)],
        ['gsm', parseFloat(gsm)],
        ['huisdieren', parseFloat(huisdieren)],
        ['elektriciteit', parseFloat(elektriciteit)],
        ['huis', parseFloat(huis)],
        ['water', parseFloat(water)],
        ['internet', parseFloat(internet)],
        ['meubels', parseFloat(meubels)],
        ['supplies', parseFloat(supplies)],
        ['vuilnis', parseFloat(vuilnis)],
        ['games', parseFloat(games)],
        ['sport', parseFloat(sport)],
        ['tekenen', parseFloat(tekenen)],
        ['reizen', parseFloat(reizen)],
        ['tuin', parseFloat(tuin)],
        ['events', parseFloat(events)],
        ['lezen', parseFloat(lezen)],
        ['tv', parseFloat(tv)],
        ['onderwijs', parseFloat(onderwijs)],
        ['charity', parseFloat(charity)],
        ['belasting', parseFloat(belasting)],
        ['gift', parseFloat(gift)],
        ['interest', parseFloat(interest)]
    ]);
    var options = {'backgroundColor':"#ffffff",
    colors: ['rgb(47, 203, 255)', 'rgb(47, 203, 255)', 'rgb(243, 255, 80)', 'rgb(243, 255, 80)', 'rgb(255, 41, 51)', 'rgb(255, 41, 51)', 'rgb(66, 255, 129)', 'rgb(66, 255, 129)', 'rgb(66, 255, 129)', 'rgb(66, 255, 129)', 'rgb(66, 255, 129)', 'rgb(66, 255, 129)', 'rgb(248, 145, 61)', 'rgb(248, 145, 61)', 'rgb(248, 145, 61)', 'rgb(248, 145, 61)', 'rgb(248, 145, 61)', 'rgb(248, 145, 61)', 'rgb(248, 145, 61)', 'rgb(218, 98, 255)', 'rgb(218, 98, 255)', 'rgb(218, 98, 255)', 'rgb(218, 98, 255)', 'rgb(218, 98, 255)', 'rgb(218, 98, 255)', 'rgb(218, 98, 255)', 'rgb(218, 98, 255)', 'rgb(73, 230, 183)', 'rgb(73, 230, 183)', 'rgb(73, 230, 183)', 'rgb(73, 230, 183)', 'rgb(73, 230, 183)']};
    var chart = new google.visualization.PieChart(document.getElementById('test'));
    chart.draw(data, options);
};
function drawCat(){
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Categorie');
    data.addColumn('number', 'bedrag');
    data.addRows([
        ['loon', parseFloat(loon)],
        ['bonus', parseFloat(bonus)],
        ['geschenken', parseFloat(geschenken)],
        ['zakgeld', parseFloat(zakgeld)],
        ['erfenis', parseFloat(erfenis)],
        ['klusjes', parseFloat(klusjes)],
        ['terugbetaling', parseFloat(terugbetaling)],
        ['beurs', parseFloat(beurs)],
        ['ziekteverzekering', parseFloat(ziekteverzekering)],
        ['loon eigen onderneming', parseFloat(loon3)],
        ['dividend eigen onderneming', parseFloat(dividend2)],
        ['huur', parseFloat(huur)],
        ['dividend', parseFloat(dividend)],
        ['interest', parseFloat(interest1)],
        ['verkoop', parseFloat(verkoop)],
        ['andere', parseFloat(interest1)]
    ]);
    var options = {'backgroundColor':"#ffffff",
    colors: ['rgb(248, 145, 61)', 'rgb(248, 145, 61)', 'rgb(66, 255, 129)', 'rgb(66, 255, 129)', 'rgb(66, 255, 129)', 'rgb(66, 255, 129)', 'rgb(243, 255, 80)', 'rgb(243, 255, 80)', 'rgb(243, 255, 80)', 'rgb(47, 203, 255)', 'rgb(47, 203, 255)', 'rgb(255, 41, 51)', 'rgb(255, 41, 51)', 'rgb(73, 230, 183)', 'rgb(73, 230, 183)', 'rgb(73, 230, 183)']};
    var chart = new google.visualization.PieChart(document.getElementById('inkomst-g'));
    chart.draw(data, options);
};
function drawCash(){
    var data = google.visualization.arrayToDataTable([
        ['Maand', 'Inkomst', { role: 'style' }, 'Uitgave'],
        [((1 + maand) % 12 + 1).toString(), totalI11, "green", -total11],
        [((2 + maand) % 12 + 1).toString(), totalI10, "green", -total10],
        [((3 + maand) % 12 + 1).toString(), totalI9, "green", -total9],
        [((4 + maand) % 12 + 1).toString(), totalI8, "green", -total8],
        [((5 + maand) % 12 + 1).toString(), totalI7, "green", -total7],
        [((6 + maand) % 12 + 1).toString(), totalI6, "green", -total6],
        [((7 + maand) % 12 + 1).toString(), totalI5, "green", -total5],
        [((8 + maand) % 12 + 1).toString(), totalI4, "green", -total4],
        [((9 + maand) % 12 + 1).toString(), totalI3, "green", -total3],
        [((10 + maand) % 12 + 1).toString(), totalI2, "green", -total2],
        [((11 + maand) % 12 + 1).toString(), totalI1, "green", -total1],
        [((12 + maand) % 12 + 1).toString(), totalI0, "green", -total0]
    ]);
    var options = {'backgroundColor':"#ffffff",
                    isStacked: true,
                    legend: { position: "none" }};
    var chart = new google.visualization.ColumnChart(document.getElementById('cash-graph'));
    chart.draw(data, options);
}
function drawInk(){
    datalist = [['Maand', 'Beleggingen', 'Cash']];
    for (i=0; i<(year-2016); i++){
        datalist.push([(year-i).toString(), totalB[i], totalC[i]])
    }
    var data = google.visualization.arrayToDataTable(datalist);
    var options = {'backgroundColor':"#ffffff",
                    isStacked: true,
                    legend: { position: "none" }};
    var chart = new google.visualization.SteppedAreaChart(document.getElementById('ink-graph'));
    chart.draw(data, options);
}
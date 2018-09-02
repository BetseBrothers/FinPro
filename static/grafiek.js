document.getElementById("title").onclick =function(){
    if (document.getElementById("test").innerHTML == ""){
        google.charts.load("current", {packages: ['corechart']});
        google.charts.setOnLoadCallback(drawChart);
    }
    else if (document.getElementById("test").style.display == "none"){
        document.getElementById("test").style.display = "block";
    }
    else {
        document.getElementById("test").style.display = "none";
    }
};
function drawChart(){
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Categorie');
    data.addColumn('number', 'bedrag');
    data.addRows([
        ['winkel', parseFloat(winkel)],
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
    var options = {'backgroundColor':"#ffffff"};
    var chart = new google.visualization.PieChart(document.getElementById('test'));
    chart.draw(data, options);
}
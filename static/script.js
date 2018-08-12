setInterval(function(){
    var time = new Date();
    var timestamp = time.toLocaleTimeString();
    document.getElementById('timestamp').innerHTML = timestamp
}, 1000);

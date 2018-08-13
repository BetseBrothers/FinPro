setInterval(function(){
    var time = new Date();
    var timestamp = time.toLocaleTimeString();
    document.getElementById('timestamp').innerHTML = timestamp
}, 1000);

function isEmpty(){
    for (i = 0; i < document.getElementById("form").children.length - 1; i++)
        if (document.getElementById("form").children[i].value == ""){
            return true;
        }
    return false;
}

document.getElementById("form").onsubmit = function(){
    if (isEmpty()){
        alert("Need to fill in form")
        return false;
    }
    else{return true}
};
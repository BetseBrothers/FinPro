setInterval(function displayCategorie(){
    if (document.getElementById("form").soort.value == "shmekkels"){
        document.getElementById("shmekkelCategorie").style.display = "flex";
        document.getElementById("inkomstCategorie").style.display = "none";
        document.getElementById("uitgaveCategorie").style.display = "none";
    }
    else if (document.getElementById("form").soort.value == "Inkomst"){
        document.getElementById("shmekkelCategorie").style.display = "none";
        document.getElementById("inkomstCategorie").style.display = "flex";
        document.getElementById("uitgaveCategorie").style.display = "none";
    }
    else if (document.getElementById("form").soort.value == "Uitgave"){
        document.getElementById("shmekkelCategorie").style.display = "none";
        document.getElementById("inkomstCategorie").style.display = "none";
        document.getElementById("uitgaveCategorie").style.display = "flex";
        if (document.getElementById("form").Categorie.value == "woning"){
            document.getElementById("voedingC").style.display = "none";
            document.getElementById("transportC").style.display = "none";
            document.getElementById("woningC").style.display = "flex";
            document.getElementById("hobbiesC").style.display = "none";
            document.getElementById("andereC").style.display = "none";
        }
        else if (document.getElementById("form").Categorie.value == "voeding"){
            document.getElementById("voedingC").style.display = "flex";
            document.getElementById("transportC").style.display = "none";
            document.getElementById("woningC").style.display = "none";
            document.getElementById("hobbiesC").style.display = "none";
            document.getElementById("andereC").style.display = "none";
        }
        else if (document.getElementById("form").Categorie.value == "transport"){
            document.getElementById("voedingC").style.display = "none";
            document.getElementById("transportC").style.display = "flex";
            document.getElementById("woningC").style.display = "none";
            document.getElementById("hobbiesC").style.display = "none";
            document.getElementById("andereC").style.display = "none";
        }
        else if (document.getElementById("form").Categorie.value == "hobbies"){
            document.getElementById("voedingC").style.display = "none";
            document.getElementById("transportC").style.display = "none";
            document.getElementById("woningC").style.display = "none";
            document.getElementById("hobbiesC").style.display = "flex";
            document.getElementById("andereC").style.display = "none";
        }
        else if (document.getElementById("form").Categorie.value == "andere"){
            document.getElementById("voedingC").style.display = "none";
            document.getElementById("transportC").style.display = "none";
            document.getElementById("woningC").style.display = "none";
            document.getElementById("hobbiesC").style.display = "none";
            document.getElementById("andereC").style.display = "flex";
        }
        else {
            document.getElementById("voedingC").style.display = "none";
            document.getElementById("transportC").style.display = "none";
            document.getElementById("woningC").style.display = "none";
            document.getElementById("hobbiesC").style.display = "none";
            document.getElementById("andereC").style.display = "none";
        }
    }
    else {
        document.getElementById("shmekkelCategorie").style.display = "none";
        document.getElementById("inkomstCategorie").style.display = "none";
        document.getElementById("uitgaveCategorie").style.display = "none";
    }

    if (document.getElementById("form").Categorie.value == "woning"){
        document.getElementById("voedingC").style.display = "none";
        document.getElementById("transportC").style.display = "none";
        document.getElementById("woningC").style.display = "flex";
        document.getElementById("hobbiesC").style.display = "none";
        document.getElementById("andereC").style.display = "none";
    }
    else if (document.getElementById("form").Categorie.value == "voeding"){
        document.getElementById("voedingC").style.display = "flex";
        document.getElementById("transportC").style.display = "none";
        document.getElementById("woningC").style.display = "none";
        document.getElementById("hobbiesC").style.display = "none";
        document.getElementById("andereC").style.display = "none";
    }
    else if (document.getElementById("form").Categorie.value == "transport"){
        document.getElementById("voedingC").style.display = "none";
        document.getElementById("transportC").style.display = "flex";
        document.getElementById("woningC").style.display = "none";
        document.getElementById("hobbiesC").style.display = "none";
        document.getElementById("andereC").style.display = "none";
    }
    else if (document.getElementById("form").Categorie.value == "hobbies"){
        document.getElementById("voedingC").style.display = "none";
        document.getElementById("transportC").style.display = "none";
        document.getElementById("woningC").style.display = "none";
        document.getElementById("hobbiesC").style.display = "flex";
        document.getElementById("andereC").style.display = "none";
    }
    else if (document.getElementById("form").Categorie.value == "andere"){
        document.getElementById("voedingC").style.display = "none";
        document.getElementById("transportC").style.display = "none";
        document.getElementById("woningC").style.display = "none";
        document.getElementById("hobbiesC").style.display = "none";
        document.getElementById("andereC").style.display = "flex";
    }
    else {
        document.getElementById("voedingC").style.display = "none";
        document.getElementById("transportC").style.display = "none";
        document.getElementById("woningC").style.display = "none";
        document.getElementById("hobbiesC").style.display = "none";
        document.getElementById("andereC").style.display = "none";
    }
}, 100);
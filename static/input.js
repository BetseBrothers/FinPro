setInterval(function displayCategorie(){
    if (document.getElementById("form").soort.value == "Inkomst"){
        document.getElementById("inkomstCategorie").style.display = "flex";
        document.getElementById("uitgaveCategorie").style.display = "none";
        document.getElementById("voedingC").style.display = "none";
        document.getElementById("transportC").style.display = "none";
        document.getElementById("woningC").style.display = "none";
        document.getElementById("utilitiesC").style.display = "none";
        document.getElementById("hobbiesC").style.display = "none";
        document.getElementById("healthC").style.display = "none";
        document.getElementById("andereC").style.display = "none";
        if (document.getElementById("form").Categorie.value == "loon"){
            document.getElementById("loonC").style.display = "flex";
            document.getElementById("thuisC").style.display = "none";
            document.getElementById("terugbetalingC").style.display = "none";
            document.getElementById("beleggingenC").style.display = "none";
            document.getElementById("ondernemingC").style.display = "none";
            document.getElementById("variaC").style.display = "none";
        }
        else if (document.getElementById("form").Categorie.value == "thuis"){
            document.getElementById("loonC").style.display = "none";
            document.getElementById("thuisC").style.display = "flex";
            document.getElementById("terugbetalingC").style.display = "none";
            document.getElementById("beleggingenC").style.display = "none";
            document.getElementById("ondernemingC").style.display = "none";
            document.getElementById("variaC").style.display = "none";
        }
        else if (document.getElementById("form").Categorie.value == "terugbetaling"){
            document.getElementById("loonC").style.display = "none";
            document.getElementById("thuisC").style.display = "none";
            document.getElementById("terugbetalingC").style.display = "flex";
            document.getElementById("beleggingenC").style.display = "none";
            document.getElementById("ondernemingC").style.display = "none";
            document.getElementById("variaC").style.display = "none";
        }
        else if (document.getElementById("form").Categorie.value == "beleggingen"){
            document.getElementById("loonC").style.display = "none";
            document.getElementById("thuisC").style.display = "none";
            document.getElementById("terugbetalingC").style.display = "none";
            document.getElementById("beleggingenC").style.display = "flex";
            document.getElementById("ondernemingC").style.display = "none";
            document.getElementById("variaC").style.display = "none";
        }
        else if (document.getElementById("form").Categorie.value == "onderneming"){
            document.getElementById("loonC").style.display = "none";
            document.getElementById("thuisC").style.display = "none";
            document.getElementById("terugbetalingC").style.display = "none";
            document.getElementById("beleggingenC").style.display = "none";
            document.getElementById("ondernemingC").style.display = "flex";
            document.getElementById("variaC").style.display = "none";
        }
        else if (document.getElementById("form").Categorie.value == "varia"){
            document.getElementById("loonC").style.display = "none";
            document.getElementById("thuisC").style.display = "none";
            document.getElementById("terugbetalingC").style.display = "none";
            document.getElementById("beleggingenC").style.display = "none";
            document.getElementById("ondernemingC").style.display = "none";
            document.getElementById("variaC").style.display = "flex";
        }
        else {
            document.getElementById("loonC").style.display = "none";
            document.getElementById("thuisC").style.display = "none";
            document.getElementById("terugbetalingC").style.display = "none";
            document.getElementById("beleggingenC").style.display = "none";
            document.getElementById("ondernemingC").style.display = "none";
            document.getElementById("variaC").style.display = "none";
        }
    }
    else if (document.getElementById("form").soort.value == "Uitgave"){
        document.getElementById("inkomstCategorie").style.display = "none";
        document.getElementById("uitgaveCategorie").style.display = "flex";
        document.getElementById("loonC").style.display = "none";
        document.getElementById("thuisC").style.display = "none";
        document.getElementById("terugbetalingC").style.display = "none";
        document.getElementById("beleggingenC").style.display = "none";
        document.getElementById("ondernemingC").style.display = "none";
        document.getElementById("variaC").style.display = "none";
        if (document.getElementById("form").Categorie.value == "woning"){
            document.getElementById("voedingC").style.display = "none";
            document.getElementById("transportC").style.display = "none";
            document.getElementById("woningC").style.display = "flex";
            document.getElementById("utilitiesC").style.display = "none";
            document.getElementById("hobbiesC").style.display = "none";
            document.getElementById("healthC").style.display = "none";
            document.getElementById("andereC").style.display = "none";
        }
        else if (document.getElementById("form").Categorie.value == "voeding"){
            document.getElementById("voedingC").style.display = "flex";
            document.getElementById("transportC").style.display = "none";
            document.getElementById("woningC").style.display = "none";
            document.getElementById("utilitiesC").style.display = "none";
            document.getElementById("hobbiesC").style.display = "none";
            document.getElementById("healthC").style.display = "none";
            document.getElementById("andereC").style.display = "none";
        }
        else if (document.getElementById("form").Categorie.value == "transport"){
            document.getElementById("voedingC").style.display = "none";
            document.getElementById("transportC").style.display = "flex";
            document.getElementById("woningC").style.display = "none";
            document.getElementById("utilitiesC").style.display = "none";
            document.getElementById("hobbiesC").style.display = "none";
            document.getElementById("healthC").style.display = "none";
            document.getElementById("andereC").style.display = "none";
        }
        else if (document.getElementById("form").Categorie.value == "hobbies"){
            document.getElementById("voedingC").style.display = "none";
            document.getElementById("transportC").style.display = "none";
            document.getElementById("woningC").style.display = "none";
            document.getElementById("utilitiesC").style.display = "none";
            document.getElementById("hobbiesC").style.display = "flex";
            document.getElementById("healthC").style.display = "none";
            document.getElementById("andereC").style.display = "none";
        }
        else if (document.getElementById("form").Categorie.value == "andere"){
            document.getElementById("voedingC").style.display = "none";
            document.getElementById("transportC").style.display = "none";
            document.getElementById("woningC").style.display = "none";
            document.getElementById("utilitiesC").style.display = "none";
            document.getElementById("hobbiesC").style.display = "none";
            document.getElementById("healthC").style.display = "none";
            document.getElementById("andereC").style.display = "flex";
        }
        else if (document.getElementById("form").Categorie.value == "health"){
            document.getElementById("voedingC").style.display = "none";
            document.getElementById("transportC").style.display = "none";
            document.getElementById("woningC").style.display = "none";
            document.getElementById("utilitiesC").style.display = "none";
            document.getElementById("hobbiesC").style.display = "none";
            document.getElementById("healthC").style.display = "flex";
            document.getElementById("andereC").style.display = "none";
        }
        else if (document.getElementById("form").Categorie.value == "utilities"){
            document.getElementById("voedingC").style.display = "none";
            document.getElementById("transportC").style.display = "none";
            document.getElementById("woningC").style.display = "none";
            document.getElementById("utilitiesC").style.display = "flex";
            document.getElementById("hobbiesC").style.display = "none";
            document.getElementById("healthC").style.display = "none";
            document.getElementById("andereC").style.display = "none";
        }
        else {
            document.getElementById("voedingC").style.display = "none";
            document.getElementById("transportC").style.display = "none";
            document.getElementById("woningC").style.display = "none";
            document.getElementById("utilitiesC").style.display = "none";
            document.getElementById("hobbiesC").style.display = "none";
            document.getElementById("healthC").style.display = "none";
            document.getElementById("andereC").style.display = "none";
        }
    }
    else {
        document.getElementById("inkomstCategorie").style.display = "none";
        document.getElementById("uitgaveCategorie").style.display = "none";
        document.getElementById("voedingC").style.display = "none";
        document.getElementById("transportC").style.display = "none";
        document.getElementById("woningC").style.display = "none";
        document.getElementById("utilitiesC").style.display = "none";
        document.getElementById("hobbiesC").style.display = "none";
        document.getElementById("healthC").style.display = "none";
        document.getElementById("andereC").style.display = "none";
        document.getElementById("loonC").style.display = "none";
        document.getElementById("thuisC").style.display = "none";
        document.getElementById("terugbetalingC").style.display = "none";
        document.getElementById("beleggingenC").style.display = "none";
        document.getElementById("ondernemingC").style.display = "none";
        document.getElementById("variaC").style.display = "none";
    }
    
}, 100);
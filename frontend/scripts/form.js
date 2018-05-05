// Verify that URL exists

function validateForm() {
    var x = document.forms["myForm"]["fname"].value;
    if (x == "") {
        alert("URL must be filled out");
        return false;
    }

    
}
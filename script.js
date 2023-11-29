//Hamburger menu function
function hamburger() {
    var menu = document.getElementById("menu-links");   
    var logo = document.getElementById("ffc-logo");
    if (menu.style.display === "block" && logo.style.display === "none") {
    menu.style.display = "none";
    logo.style.display = "block";
    } else {
        menu.style.display = "block";
        logo.style.display = "none";
        }
    }


function validateForm() {
    var fname = document.getElementById("fName").value;
    var lname = document.getElementById("lName").value;
    var email = document.getElementById("email").value;
    var phone = document.getElementById("phone").value;
    var address = document.getElementById("address").value;
    if (fname == "") {
        window.alert("First Name must be filled out");
        return false;
    }
    if (lname == "") {
        window.alert("Last Name must be filled out");
        return false;
    }
    if (email == "") {
        window.alert("Email must be filled out");
        return false;
    }
    if (phone == "") {
        window.alert("Phone number must be filled out");
        return false;
    }
    if (address == "") {
        window.alert("Address must be filled out");
        return false;
    }
    if (fname != "" && lname != "" && email != "" && phone != "" && address != "") {
        window.alert("You have submitted the form");
        return true;
    }
}
// LOGIN POP UP

document.addEventListener("DOMContentLoaded", function() {

    const loginBtn = document.getElementById("login-btn");
    const loginPopup = document.getElementById("login-popup");
    const closeBtn = document.querySelector(".close-btn");

    // OPEN LOGIN
    loginBtn.addEventListener("click", function(event) {
        event.preventDefault();
        loginPopup.classList.add("show");
    });

    // CLOSE LOGIN
    closeBtn.addEventListener("click", function() {
        loginPopup.classList.remove("show");
    });

    // CLOSE WHEN CLICKING OUTSIDE
    loginPopup.addEventListener("click", function(event) {
        if (event.target === loginPopup) {
            loginPopup.classList.remove("show");
        }
    });

});
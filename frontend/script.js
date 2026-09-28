document.addEventListener("DOMContentLoaded", function () {

    const loginBtn = document.getElementById("login-btn");
    const signupBtn = document.querySelector(".signup-btn");

    const loginPopup = document.getElementById("login-popup");
    const loginForm = document.getElementById("login-form");
    const signupForm = document.getElementById("signup-form");

    const signupLink = document.getElementById("signup-link");
    const loginLink = document.getElementById("login-link");

    const closeBtns = document.querySelectorAll(".close-btn");


    // LOGIN BUTTON
    loginBtn.addEventListener("click", function (event) {
        event.preventDefault();

        loginPopup.classList.add("show");

        loginForm.style.display = "block";
        signupForm.style.display = "none";
    });


    // BIG SIGN UP BUTTON
    signupBtn.addEventListener("click", function () {

        loginPopup.classList.add("show");

        loginForm.style.display = "none";
        signupForm.style.display = "block";
    });


    // SIGN UP LINK INSIDE LOGIN
    signupLink.addEventListener("click", function (event) {
        event.preventDefault();

        loginForm.style.display = "none";
        signupForm.style.display = "block";
    });


    // LOGIN LINK INSIDE SIGN UP
    loginLink.addEventListener("click", function (event) {
        event.preventDefault();

        signupForm.style.display = "none";
        loginForm.style.display = "block";
    });


    // CLOSE BUTTONS
    closeBtns.forEach(function (button) {
        button.addEventListener("click", function () {
            loginPopup.classList.remove("show");
        });
    });


    // CLICK OUTSIDE POPUP TO CLOSE
    loginPopup.addEventListener("click", function (event) {

        if (event.target === loginPopup) {
            loginPopup.classList.remove("show");
        }

    });

});
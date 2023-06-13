/*selecting the wrapper element */
const wrapper = document.querySelector('.wrapper');

/*selecting  the login and register links respectively*/
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');

/*selecting the login and the close icon('x') */
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');
 

/*Adding an event listener to the register link(at the login page)*/
/*When clicked, the wrapper element gets the 'active' class added to show the registration form*/
registerLink.addEventListener('click', ()=> {
    wrapper.classList.add('active');
});

/*Adding an event listener to the login link*/
/*when clicked, the 'active' class is removed from the wrapper element to hide the registration form*/
loginLink.addEventListener('click', ()=> {
    wrapper.classList.remove('active');
});

/*Adding an event listener to the login popup button*/
/*when clicked, the wrapper element gets the 'active-popup' class added to show the login popup*/
/*in short clicking the login button at the top left of the page triggers the login popup*/
btnPopup.addEventListener('click', ()=> {
    wrapper.classList.add('active-popup');
});

/*Adding an event listener to the close icon*/
/*When clicked, the 'active-popup' class is removed from the wrapper element to close the login popup*/
/*clicking the "X" icon closes the login/registration popups*/
iconClose.addEventListener('click', ()=> {
    wrapper.classList.remove('active-popup');
});
const toggleFormButton = document.getElementById('toggleForm');
const loginForm = document.getElementById('loginForm');
const signupForm = document.getElementById('signupForm');
const formContainer = document.getElementById('formContainer');
const formTitle = document.getElementById('formTitle');

toggleFormButton.addEventListener('click', function() {
    if (formContainer.classList.contains('rotate')) {
        formContainer.classList.remove('rotate');
        formTitle.innerText = 'Login';
        toggleFormButton.innerText = 'Switch to Sign Up';
        loginForm.style.display = 'block';
        signupForm.style.display = 'none';
    } else {
        formContainer.classList.add('rotate');
        formTitle.innerText = 'Sign Up';
        toggleFormButton.innerText = 'Switch to Login';
        loginForm.style.display = 'none';
        signupForm.style.display = 'block';
    }
});
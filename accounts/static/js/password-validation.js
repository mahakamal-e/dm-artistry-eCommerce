document.addEventListener('DOMContentLoaded', function() {
    var passwordInput = document.querySelector('#id_password1');
    var minLength = document.querySelector('#min-length');
    var uppercase = document.querySelector('#uppercase');
    var lowercase = document.querySelector('#lowercase');
    var number = document.querySelector('#number');
    var specialChar = document.querySelector('#special-char');
    var requirements = document.querySelector('.password-requirements');
    
    function validatePassword() {
        var password = passwordInput.value;
        
        // Show the requirements only if password input is not empty
        if (password.length > 0) {
            requirements.style.display = 'block';
        } else {
            requirements.style.display = 'none';
        }

        minLength.classList.toggle('valid', password.length >= 8);
        minLength.classList.toggle('invalid', password.length < 8);
        
        uppercase.classList.toggle('valid', /[A-Z]/.test(password));
        uppercase.classList.toggle('invalid', !/[A-Z]/.test(password));
        
        lowercase.classList.toggle('valid', /[a-z]/.test(password));
        lowercase.classList.toggle('invalid', !/[a-z]/.test(password));
        
        number.classList.toggle('valid', /[0-9]/.test(password));
        number.classList.toggle('invalid', !/[0-9]/.test(password));
        
        specialChar.classList.toggle('valid', /[@$!%*?&]/.test(password));
        specialChar.classList.toggle('invalid', !/[@$!%*?&]/.test(password));
    }

    passwordInput.addEventListener('input', validatePassword);
});


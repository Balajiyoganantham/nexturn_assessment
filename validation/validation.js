function validateForm() {
    const email = document.getElementById("email").value;
    const age = document.getElementById("age").value;
    const emailError = document.getElementById("emailError");
    const ageError = document.getElementById("ageError");

    emailError.textContent = '';
    ageError.textContent = '';
    

    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailPattern.test(email)) {
        emailError.textContent = "Please enter a valid email address.";
        return false;
    }


    if (age < 18 || age > 100) {
        ageError.textContent = "Age must be between 18 and 100.";
        return false;
    }
    alert("Form submitted successfully!");
    return true; 



    

}

// JavaScript for opening and closing the contact modal
const contactUsButton = document.getElementById("contact-us-button");
const contactModal = document.getElementById("contact-modal");
const closeContactModal = document.getElementById("close-contact-modal");

// Open the contact modal
contactUsButton.addEventListener("click", function () {
    contactModal.style.display = "block";
});

// Close the contact modal
closeContactModal.addEventListener("click", function () {
    contactModal.style.display = "none";
});

// Close the contact modal when clicking outside of it
window.addEventListener("click", function (event) {
    if (event.target === contactModal) {
        contactModal.style.display = "none";
    }
});

// JavaScript for handling form submission
const contactForm = document.getElementById("contact-form");

contactForm.addEventListener("submit", function (e) {
    e.preventDefault(); // Prevent the form from submitting normally (page reload)

    // Get form data
    const email = document.getElementById("email").value;
    const name = document.getElementById("name").value;
    const surname = document.getElementById("surname").value;

    // Here, you can handle the email sending logic
    // For simplicity, we'll just display an alert with the submitted data
    const message = `Email: ${email}\nName: ${name}\nSurname: ${surname}`;
    alert("Submitted Data:\n" + message);

    // Close the modal after submission (you can customize this behavior)
    contactModal.style.display = "none";
});

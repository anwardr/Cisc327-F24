function validateRoleSelection() {
    console.log("Validation function is running");

    const landlord = document.getElementById('landlord').checked;  // Only check landlord
    const roleError = document.getElementById('role-error');       // Error message element

    // Check if the landlord option is selected
    if (!landlord) {
        // Show the error message if no role is selected (i.e., landlord is not checked)
        roleError.style.display = "block";
        return false; // Prevent form submission
    } else {
        // Hide the error message if the landlord option is selected
        roleError.style.display = "none";
        return true; // Allow form submission
    }
}

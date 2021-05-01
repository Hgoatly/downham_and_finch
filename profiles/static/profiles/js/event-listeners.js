var deliveryForm = document.getElementById("delivery-address-update-form");
    var addDeliveryButton = document.getElementById("add-delivery-button");
    var billingTitle = document.getElementById("billing-title");
    var profileUpdateForm = document.getElementById("profile-update-form");
    var editBillingButton = document.getElementById("edit-billing-button");
    var deliveryTitle = document.getElementById("delivery-title"); 
    
    billingTitle.style.disply = "block"
    profileUpdateForm.style.display = "block";
    addDeliveryButton.style.display = "block";
    deliveryTitle.style.display = "none";
    deliveryForm.style.display = "none";
    editBillingButton.style.display ="none";


    addDeliveryButton.addEventListener("click", function() {
        deliveryForm.style.display = "block";
        addDeliveryButton.style.display = "none";
        profileUpdateForm.style.display = "none";
        billingTitle.style.display = "none"
        editBillingButton.style.display = "block";
        deliveryTitle.style.display = "block";
    });
    
    editBillingButton.addEventListener("click", function() {
        deliveryForm.style.display = "none";
        addDeliveryButton.style.display = "block";
        profileUpdateForm.style.display = "block";
        billingTitle.style.display = "block"
        editBillingButton.style.display = "none";
        deliveryTitle.style.display = "none";    
    });
var checkoutDeliveryButton = document.getElementById("checkout-delivery-address-button");
var checkoutDeliveryForm = document.getElementById("checkout-delivery-form");

checkoutDeliveryButton.style.display = "block"
checkoutDeliveryForm.style.display = "none"

checkoutDeliveryButton.addEventListener("click", function() {
    checkoutDeliveryButton.style.display = "none"
    checkoutDeliveryForm.style.display = "block"
})


// This file is copied and adapted from the Boutique Ado project.

let countrySelected =$('#id_default_country').val();
        if(!countrySelected) {
            $('#id_default_country').css('color', '#aab7c4');
        };
        $('#id_default_country').change(function() {
            countrySelected = $(this).val()
            if(!countrySelected) {
                $(this).css('color', '#aab7c4');
            } else {
                $(this).css('color', '#000');
            }
        });

let deliveryCountrySelected =$('#id_country').val();
        if(!deliveryCountrySelected) {
            $('#id_country').css('color', '#aab7c4');
        };
        $('#id_country').change(function() {
            deliveryCountrySelected = $(this).val()
            if(!deliveryCountrySelected) {
                $(this).css('color', '#aab7c4');
            } else {
                $(this).css('color', '#000');
            }
        });
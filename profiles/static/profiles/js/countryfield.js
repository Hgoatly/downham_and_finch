// This file is copied and adapted from the Boutique Ado project.

let countrySelected =$('#id_default_country, #id_country').val();
        if(!countrySelected) {
            $('#id_default_country, #id_country').css('color', '#aab7c4');
        };
        $('#id_default_country, #id_country').change(function() {
            countrySelected = $(this).val()
            if(!countrySelected) {
                $(this).css('color', '#aab7c4');
            } else {
                $(this).css('color', '#000');
            }
        })
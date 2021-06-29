# Downham and Finch Testing:

The Downham and Finch site was tested extensively, using the following processes:

## Table of Contents:

- [Chrome Developer Tools](#Chrome-Developer-Tools)
- [Lighthouse](#Lighthouse)
- [W3c Markup Validation Service](#W3c-Markup-Validation-Service)
- [W3c CSS Validation Service](#W3c-CSS-Validation-Service)
- [JSHint](#JSHint)
- [Automated Testing](#Automated-Testing)
- [Testing the User Stories](#Testing-the-User-Stories)
    - [Create](#)


### Chrome Developer Tools:

- Chrome developer tools was used regularly to check the layout, and to check the console for errors.

### Lighthouse:

- The 'Lighthouse' function in Chrome Developer Tools was used to check the site's performance.

<img src="static/testing_images/lighthouse.jpg">

### W3C Markup Validation Service:

- The W3C Markup Validation Service was used to check that HTML used for the site was compliant with modern standards. 
The code passed the validator's tests with no errors or warnings:

<img src="static/testing_images/w3_html.jpg">

### W3c CSS Validation Service:

- The W3C CSS Validation Service was used to check that HTML used for the site was compliant with modern standards. 
The code passed the validator's tests with no errors:

<img src="static/testing_images/w3_css.jpg">

There were, however, a number of warnings. These mainly related to the use of 'allauth' - so were beyond my control.
There were additional warnings due to the use of 'zoom' that was used to make the images aesthetically pleasing on the site.

<img src="static/testing_images/w3_css_warnings.jpg">

### Automated Testing:

- Automated tests were written for the following apps. They can be found in their respective app folders:
    - About (forms and views)
    - Basket (views)
    - Blog (forms, models and views)
    - Checkout (forms and views)
    - Contact (forms and views)
    - Faq (forms, models and views)
    - Home (views)
    - Products (forms, models, views)
    - Reviews (forms and views)

All tests passed with no issues.



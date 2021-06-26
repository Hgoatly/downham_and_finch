# Downham and Finch
- An e commerce site selling custom face masks, pet bandanas and pet bow ties.

## **Table of Contents:**

- [Site Owner Goals](#site-owner-goals)
- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
    - [First Time Visitor Goals](#first-time-visitor-goals)
    - [Returning Visitor Goals](#returning-visitor-goals)
    - [Frequent Visitor Goals](#frequent-visitor-goals)
  - [Design](#Design)
    - [Imagery](#imagery)
    - [Colours Used](#colours-used)
    - [Typography](#typography) 
    - [Layout](#layout)
        - [Accessible to all users via the navbar](#Accessible-to-all-users-via-the-navbar)
        - [Accessible to all users via the search boxes](#Accessible-to-all-users-via-the-search-boxes)
        - [Accessible to registered users via the navbar](#Accessible-to-registered-users-via-the-navbar)
        - [Accessible to registered users via the My Profile page](#Accessible-to-registered-users-via-the-My-Profile-page)
        - [Accessible to registered users via the Manage Account page](#Accessible-to-registered-users-via-the-Manage-Account-page)
        - [Accessible only to the site owner (admin user)](#Accessible-only-to-the-site-owner-(admin-user))
        - [Error Pages](#Error-Pages)
        - [Additional features available to logged in users](#Additional-features-available-to-logged-in-users)
        - [Additional features available to any user who is not logged in](#Additional-features-available-to-any-user-who-is-not-logged-in)
    - [Wireframes](#wireframes)
  - [Features](#features)
    - [Mobile Design Features](#mobile-design-features)
    - [Tablet Design Features](#tablet-design-features)
    - [Desktop Design Features](#desktop-design-features)
    - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries and Other Sources Used](#frameworks,-libraries-and-other-sources-used)
- [Information Architecture](#information-architecture)
    - [Database Choice](#database-choice)
- [Testing](#testing)
  - [Known Bugs and Fixes](#known-bugs-and-fixes)
  - [Defensive Programming](#defensive-programming)
- [Deployment](#deployment)
  - [Github Pages](#github-pages)
  - [Forking The Repository](#forking-the-repository)
  - [Making A Local Clone](#making-a-local-clone)
- [Credits](#credits)
- [Version Control](#version-control)


## Site Owner Goals:

1. The site owner's primary goal is to sell their products to new and returning customers.
2. The secondary goal is to showcase new products that are available to new and returning customers. 

## User Stories:

### New Users:
1. I would like to be able to browse the site and make a purchase.
2. I would like to register for an account so that I can create a profile, and so that my details will be stored for future visits..
3. I would like to search the site so that I can find specific products.

### Returning Users:
4. I would like to be able to login to the site so that I can view/update my profile.
5. I would like to be able to browse and search the site for new products that have been added to the site since my last visit.

### All Users:
6. I would like to be able to reset my password should I forget it.
7. I would like to be able to contact the site owner, so that I can ask a question, or make a complaint or a compliment.
8. I would like to be able to submit a review of the product. 
9. I would like to be abe to login to the site with my Facebook account.
10. I would like to be able to pay for my purchases securely using Apple Pay.
11. I would like to be able to pay for my purchases securely using PayPal.


## Design:

### Imagery:

- On the landing page, the Hero image is one of lots of small birds. They represent 'Finch' in the name of the company, as a finch is a small bird that is very 
similar to those in the image.

![Downham and Finch Hero Image](media/hero_image.jpg)

- All product images were sent by the site owner, or were downloaded from [unsplash](https://www.unsplash.com/).

### Colours Used:

- Black (#000) was chosen as the background colour for the navbar, footer, hero image logo and call to action buttons because it contrasts well with the 
hero image. 

- Gold (#D4AF37) was used for all text and icons that are on the black background as it goes well with the hero image, as well as making a good contrast 
with the black background.

- White (#fff) was used as the backgorund, and black (#000) was used for the text on all pages other than the landing page so that the background and text do 
not detract from the products displayed.


### Typography:

- 'Parisienne' was chosen for all logo elements and page titles as it is striking, and appropriate for a logo.
- 'Open Sans' was chosen for all other text because it's clean and easy to read.


### Layout: 

#### Accessible to all users via the navbar:

- All Pages:
- **About** dropdown with the following options:
    - **About**: A short biography of the company.
    - **Blog**: Latest news and information about the company, and its products. The site owner is able to add, edit and delete blog posts from here, 
    but other users may only read the posts.
    - **Faqs**: Frequently asked questions. The site owner is able to add, edit and delete blog posts from here, but other users may only read the posts.
    Other site visitors may submit a question by clicking on the 'contact us' link. The question can then be added by the site owner, once it has been 
    approved. This is in order to safeguard against inappropriate or offensive questions being submitted.
    - **Reviews**: All product reviews are listed here.  
    - **Contact**: Contact the business owner via a contact form.
- **My Account**: 
    - **Login**: Login for existing users.
    - **Register**: Register as a user.
- **Shopping Basket**:
    - **Shopping Basket Icon**: Click here to navigate to the shopping basket page.
- **Search**: Search the site using key words.
- **All Products** dropdown with the following options:
    - **By Price**: Display items by price.
    - **By Product Type**: Display items by Product Type.
    - **All Products**: Display all products.
- **Face Masks** dropdown with the following product options:
    - **3D Masks**: Show a selection of 3D face masks.
    - **Simple Masks**: Show a selection of Simple Maks.
    -**All Face Masks**: Show all Face Masks
- **Pet Products** dropdown with the following options:
    - **Pet Bandanas**: Show all pet bandanas.
    - **Pet Bow Ties**: Show all pet bow ties.
    - **All Pet Products**: Show all pet products.
- **Bags** dropdown with the following options:
    - **Lavender Bags**: Show all lavender bags.
    - **Drawstring Bags**: Show all drawstring bags.

#### Accessible to logged in regisered users via the Navbar:

-**My Account**:
    -**My Profile**: Navigate to the session user's profile page.
    -**Logout**: Log out of the site.

#### Accessible only to Superusers(Admin) via the navbar:

-**Product Management**: Add products to the site.

#### Accessible to all users via the Footer:

- **Social Media** links to the following social media sites:
    - **Facebook**
    - **Twitter**
    - **Instagram**
- **Products**: Links to available products.
    -**Face Masks**: Show all Face Masks.
    - **Pet Products**: Show all Pet Products.    
    - **Lavender Bags**: Show all lavender bags.
    - **Drawstring Bags**: Show all drawstring bags.
-**Useful Links**:
    -**About**: Navigates to the About page.
    -**Faqs**: Navigates to the Faqs page.
    -**Reviews**: Navigates to the Reviews page.
    -**Contact**: Navigates to the Contact page.
-**Contact**:
    -**Email Us**: Navigates to the Contact page.
    -**Phone Number**: Allows the user to call the business by clicking on the number.

#### Accessible to all users on the Products page:

-**Sort Box**: Allows the user to sort the items by price, rating, name and category.

#### Accessible to Superusers(Admin) on the Products page:

-**Edit**: Allows a superuser to edit a product.
-**Delete**: ALlows a superuser to delete a product.

#### Accessible to Superusers(Admin) on the Product Detail page:

-**Edit**: Allows a superuser to edit a product.
-**Delete**: Allows a superuser to delete a product.

#### Accessible to Superusers(Admin) on the About page:















### Wireframes

- The Downham and Finch sitemap can be found <a href="static/wireframes/downham-and-finch-sitemap.pdf" target="_blank">here.</a>

- Original desktop wireframes from 04/04/21 can be found <a href="static/wireframes/downham-and-finch-desktop-wireframes.pdf" target="_blank">here.</a>

- Original tablet wireframes from 04/04/21 can be found <a href="static/wireframes/downham-and-finch-tablet-wireframes.pdf" target="_blank">here.</a>

- Original mobile wireframes from 04/04/21 can be found <a href="static/wireframes/downham-and-finch-mobile-wireframes.pdf" target="_blank">here.</a>


## Technologies used:

### languages Used:

- HTML5
- CSS3
- Javascript
- Python

### Frameworks, Libraries and Other Sources Used:

- [Django](https://www.djangoproject.com/) was used as the principal framework for the project.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used for all forms on the site.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) was used for user authentication on the site.
- [Stripe](https://stripe.com/) was used to handle payments on the site.
- [Bootstrap4](https://getbootstrap.com/) was used to aid reponsive design.
- [Amazon Web Services](https://aws.amazon.com/) S3 was used to store all static CSS and Javascript files, and images.
- [SQLite3](https://www.sqlite.org/index.html) is the database that was used in production.
- [PostgreSQL](https://www.postgresql.org/) is the database used by the deployed site.
- [Heroku](https://www.heroku.com/) hosts the Downham and Finch website.
- [JQuery](https://jquery.com/) was used extensively throughout the site, in order to provide functionality for Bootstrap elements, and for Stripe. 
- [GitPod](https://gitpod.io/) was used as an IDE for this project. 
- [GitHub](https://github.com/) is where the Downham and Finch's repository is stored. Regular commits were made throughout, and code was pushed to GitHub from GitPod.

## Deployment:

### Heroku deployment with AWS:

- The Downham and Finch website was deployed to [Heroku](https://www.heroku.com/) using the following steps:

1. Install gunicorn, psycopg2-binary and dj-database-url using the ```PIP Install``` command.
2. Freeze all the requirements for the project into a requirements.txt file using the ```pip3 freeze > requirements.txt``` command.
3. Create a procfile, with the following inside it: ```web: gunicorn downham_and_finch.wsgi:application```.
4. Push these changes to GitHub, using ```git add .```, ```git commit -m``` and ```git push``` commands.
5. Navigate to [Heroku](https://www.heroku.com/), and login or create an account.
6. Once logged in, click on 'resources'.
7. From the add-ons search bar, add the Heroku Postgres DB, select the free account, and then submit order form to add it to the project.
8. From the app's dashboard, click on 'settings', and then 'reveal config vars' in order to set the necessary configuration variables for the project.

| Key                   | Value                      |
|-----------------------|----------------------------|
| AWS_ACCESS_KEY_ID     | Your AWS Access Key        |
| AWS_SECRET_ACCESS_KEY | Your AWS Secret Access Key |
| DATABASE_URL          | Your Database URL          |
| EMAIL_HOST_PASS       | Your Email Password        |
| EMAIL_HOST_USER       | Your Email Address         |
| SECRET_KEY            | Your Secret Key            |
| STRIPE_PUBLIC_KEY     | Your Stripe Public Key     |
| STRIPE_SECRET_KEY     | Your Stripe Secret Key     |
| STRIPE_WH_SECRET      | Your Stripe WH Key         |
| USE_AWS               | TRUE                       |

## Acknowledgements:

- **My Mentor** Can Sücüllü, for help and guidance on this project.
- **My Friends and Family** for constant support, and feedback on the content and functionality.
- **Code Institute Slack Channel** for help answering my many questions.
- **Code Institute Tutor Support** for helping me work out why things weren't working how they should. In particular, Tim, Shirley, Scott, Igor and Jo for their kindness and patience. 


## Version Control: 

- Throughout the development process, regular commits have been made in Gitpod, which have been pushed to the Recipes Without Github repository.
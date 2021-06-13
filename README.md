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
    - [Colours Used](#colours-used)
    - [Typography](#typography) 
    - [Imagery](#imagery)
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
  - [Application Programming Interfaces Used (APIs)](#application-programming-interfaces-used-(APIs))
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


## Acknowledgements:

- **My Mentor** Can Sücüllü, for help and guidance on this project.
- **My Friends and Family** for constant support, and feedback on the content and functionality.
- **Code Institute Slack Channel** for help answering my many questions.
- **Code Institute Tutor Support** for helping me work out why things weren't working how they should. In particular, Tim, Shirley, Scott, Igor and Jo for their kindness and patience. 


## Version Control: 

- Throughout the development process, regular commits have been made in Gitpod, which have been pushed to the Recipes Without Github repository.
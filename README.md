<div align="center">

# **Downham and Finch**

<img src="static/readme_images/hero_photo.jpg">

An e commerce site selling custom face masks, pet products, lavender and drawstring bags.

Visit [Downham and Finch](https://downham-and-finch.herokuapp.com/)
</div>

## **Table of Contents:**

- [Site Owner Goals](#site-owner-goals)
- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
    - [All Users](#All-Users)
    - [Registered Users](#Registered-Users)
    - [Siteowner](#Siteowner)
    - [First Time Visitor Goals](#first-time-visitor-goals)
    - [Returning Visitor Goals](#returning-visitor-goals)
  - [Design](#Design)
    - [Imagery](#imagery)
    - [Colours Used](#colours-used)
    - [Typography](#typography) 
    - [Layout](#layout)
        - [Accessible to all users via the navbar](#Accessible-to-all-users-via-the-navbar)
        - [Accessible to logged in regisered users via the Navbar](#Accessible-to-logged-in-regisered-users-via-the-Navbar)
        - [Accessible only to Superusers(Admin) via the navbar](#Accessible-only-to-Superusers(Admin)-via-the-navbar)
        - [Accessible to all users via the Footer](#Accessible-to-all-users-via-the-Footer)
        - [Accessible to all users on the Products page](#Accessible-to-all-users-on-the-Products-page)
        - [Accessible to Superusers(Admin) on the Products page](#Accessible-to-Superusers(Admin)-on-the-Products-page)
        - [Accessible to Superusers(Admin) on the Product Detail page](#Accessible-to-Superusers(Admin)-on-the-Product-Detail-page)
        - [Accessible to Superusers(Admin) on the About page](#Accessible-to-Superusers(Admin)-on-the-About-page)
        - [Accessible to Superusers(Admin) on the Blog page](#Accessible-to-Superusers(Admin)-on-the-Blog-page)
        - [Accessible to Superusers(Admin) on the Faqs page](#Accessible-to-Superusers(Admin)-on-the-Faqs-page)
        - [Accessible to Superusers(Admin) on the Reviews page](#Accessible-to-Superusers(Admin)-on-the-Reviews-page)
        - [Error Pages](#Error-Pages)
    - [Wireframes](#wireframes)
  - [Features](#features)
    - [Mobile Design Features](#mobile-design-features)
    - [Tablet Design Features](#tablet-design-features)
    - [Desktop Design Features](#desktop-design-features)
    - [Interactive Features](#Interactive-Features)
    - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries and Other Sources Used](#frameworks,-libraries-and-other-sources-used)
- [Information Architecture](#information-architecture)
    - [Database Choice](#database-choice)
    - [Data Modeling](#Data-Modeling)
- [Testing](#testing)
  - [Known Bugs and Fixes](#known-bugs-and-fixes)
  - [Defensive Programming](#defensive-programming)
- [Deployment](#deployment)
  - [Heroku Deployment with AWS](#github-pages)
  - [Amazon Web Services](#forking-the-repository)
  - [Making A Local Clone](#making-a-local-clone)
- [Credits](#credits)
- [Version Control](#version-control)

# UX:

## Site Owner Goals:

The Downham and Finch website is a real world application, designed for friends Helen Downham and Emily Finch, as a way of selling 
and marketing their handmade textile products.

1. The site owner's primary goal is to sell their products to new and returning customers.
2. The secondary goal is to showcase new products that are available to new and returning customers. 

## User Stories:

### All Users:
1. I would like to be able to browse the site, and view items, so that I can purchase them.
2. I would like to be able to view individual product details, so that I can confirm whether the product is suitable
3. I would like to search the site so that I can find specific products.
4. I would like to be able to sort the items by price, product name, and product category, so that I can quickly identify products that I am interested in.
5. I would like to easily be able to view my search results, so that I can quickly identify products that I am interested in.
6. I would like to be able to contact the site owner, so that I can ask a question, or make a complaint or a compliment.
7. I would like to be able to register for an account, so that I can view past orders, and view and update my billing details.
8. I would like to be able to read about the company, so that I can find out more about them, and their aims.
9. I would like to be able to read a list of frequently asked questions, so that I can find answers to any questions I may have.
10. I would like to be able to read blog posts, so that I can stay in touch with any news that the company may have.
11. I would like to be able to read reviews of products, so that I know whether they are good quality before I buy them.
12. I would like to be able to make a secure payment when I place an order.
13. I would like to receive feedback about whether or not my order was successful.
14. I would like to receive an email confirmation once I have placed an order.

### Registered Users:
15. I would like to be able to login to the site so that I can view/update my profile.
16. I would like to be able to easily logout of the site.
17. I would like to be able to submit a review of a product.

### Siteowner: 
18. I would like to be able to add products to the site, so that I can upload new products as they become available. 
19. I would link to be able to edit products already on the site, so that if product information changes, I can change the existing information.
20. I would like to be able to delete products that are no longer necessary for the site.
21. I would like to be able to upload blog posts, so that I can share news and events with my customers.
22. I would like to be able to edit blog posts, so that I can add more information, or correct a typo.
23. I would like to be able to delete a blog post if it is no longer relevent.
24. I would like to be able to add frequently asked questions (faqs) to the site, so that people don't keep contacting me with the same questions.
25. I would like to be able to edit faqs, in case a question or answer needs to be changed.
26. I would like to be able to delete a faq, in case it is no longer relevent.
27. I would like to be able to delete reviews that users have posted, so that I can remove any inappropriate or offensive content that may have been posted.
28. I would like users to be able to contact me, so that they will receive good customer service.

### First Time Visitor Goals:

- I would like to browse the site and make a purchase.
- I would like to register for an account.
- I would like to learn about the company, read some reviews and faqs, and be able to contact the business owner.

### Returning Visitor Goals:

- I would like to be able to view my profile.
- I would like to be able to add a review for a product I have purchased.
- I would like to be able to browse the site for new products that may have been added since my last visit.

## Design:

### Imagery:

- On the landing page, the Hero image is one of lots of small birds. They represent 'Finch' in the name of the company, as a finch is a small bird that is very 
similar to those in the image. It was downloaded from [unsplash](https://www.unsplash.com/)

![Downham and Finch Hero Image](media/hero_image.jpg)

- The origin of all other images is detailed in the [Credits](#Credits) section,

### Colours Used:

- Black (#000) was chosen as the background colour for the navbar, footer, hero image logo and call to action buttons because it contrasts well with the 
hero image. 

- Gold (#D4AF37) was used for all text and icons that are on the black background as it goes well with the hero image, as well as making a good contrast 
with the black background.

- White (#fff) was used as the backgorund, and black (#000) was used for the text on all pages other than the landing page so that the background and text do 
not detract from the products displayed.

- Turquoise (#17a2b8) was chosen as the colour for the basket when there are items in it, as it makes a good contrast with the other colours on the site.


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

-**Edit Content**: Allows a superuser to edit the About page.

#### Accessible to Superusers(Admin) on the Blog page:

-**Edit Post**: Allows a superuser to edit a blog.
-**Delete Post**: Allows a superuser to delete a blog.

#### Accessible to Superusers(Admin) on the Faqs page:

-**Edit Faq**: Allows a superuser to edit a faq.
-**Delete Faq**: Allows a superuser to delete a Faq.

#### Accessible to Superusers(Admin) on the Reviews page:

-**Edit Review**: Allows a superuser to edit a faq.
-**Delete Review**: Allows a superuser to delete a Faq.

### Error Pages:

-**404 Error Page**: A custom 404 error page was designed to redirect users back to the site in the event of a 404 error.

-**500 Error Page**: A custom 505 error page was designed to redirect users back to the site in the event of a 500 error.


### Wireframes:

- The original Downham and Finch sitemap can be found here <a href="static/wireframes/downham-and-finch-sitemap.pdf" target="_blank">here.</a>

- Original desktop wireframes from 04/04/21 can be found here <a href="static/wireframes/downham-and-finch-desktop-wireframes.pdf" target="_blank">here.</a>

- Original tablet wireframes from 04/04/21 can be found here <a href="static/wireframes/downham-and-finch-tablet-wireframes.pdf" target="_blank">here.</a>

- Original mobile wireframes from 04/04/21 can be found here <a href="static/wireframes/downham-and-finch-mobile-wireframes.pdf" target="_blank">here.</a>

- The final Downham and Finch sitemap can be found here <a href="static/wireframes/downham-and-finch-final-sitemap.pdf" target="_blank">here.</a>

- Original desktop wireframes from 04/04/21 can be found here <a href="static/wireframes/downham-and-finch-final-desktop-wireframes.pdf" target="_blank">here.</a>

- Original tablet wireframes from 04/04/21 can be found here <a href="static/wireframes/downham-and-finch-final-tablet-wireframes.pdf" target="_blank">here.</a>

- Original mobile wireframes from 04/04/21 can be found here <a href="static/wireframes/downham-and-finch-final-mobile-wireframes.pdf" target="_blank">here.</a>

### Features:

#### Mobile Design Features:

The Downham and Finch website follows the principles of mobile-first, responsive design. With this in mind, the following features on the mobile site differ 
from those on larger screens.

- The navbar has been collapsed, and is accessed by clicking on the 'hamburger' icon in the top left hand corner of the screen. When the 'hamburger'
icon is clicked, the 'All Products', 'Face Masks', 'Pet Products' and 'bags' links are displayed, as well as a 'home' link.

- The Search box has been replaced by an icon, which displays a search box when clicked.

- The 'Search', 'About', 'My Account' and 'Basket' icons have had their padding reduced, so that they fit on one line.

- The product images on the products page are displayed one per row, in order to make best use of space, and to be visually appealing.

#### Tablet Design Features:

The tablet design has most of the same features as the mobile site, except those detailed below:

- The products are displayed two products per row, rather than 4 on the desktop site, and 1 on the mobile site.

#### Desktop Design Features:

The desktop design has some of the same features as the obile and tablet versions. The differences are detailed below:

- The fixed navbar is not collapsed, and spans the width of the page.

- Products on the products page are displayed with 4 products per row.

#### Interactive Features:

The Downham and Finch website has been built around the principles of CRUD (Create, Read, Update, Delete), and all of these actions can be taken on 
the site:

- **Register**: The site visitor can add their details to open an account on the site.
- **Login**: The site visitor can login to the site if they are an existing user.
- **Contact**: Any User can contact the site owner by email.
- **Sort**: Any user can sort the products by price, name or category.
- **Search**: Any user can search the site using keywords.
- **Checkout**: Any user can make a secure purchase using Stripe.
- **Add Product**: The superuser (Admin) can add products to the database.
- **Edit Product**: The superuser (Admin) can edit products that are already in the database.
- **Delete Product**: The superuser (Admin) can delete products that are already in the database.
- **Edit Content**: The superuser (Admin) can edit the content on the 'About' page.
- **Add Blog**: The superuser (Admin) can add a post to the 'Blog page'.
- **Edit Blog**: The superuser (Admin) can edit a blog post.
- **Delete Blog**: The superuser (Admin) can delete a blog post.
- **Add Faq**: The superuser (Admin) can add a Faq.
- **Edit Faq**: The superuser (Admin) can edit a Faq.
- **Delete Faq**: The superuser (Admin) can delete a Faq.
- **Add Review**: A logged in and registered user can add a review.
- **Delete Review**: The superuser (Admin) can delete a review.
- **About**: The Superuser (Admin) can update the 'About' section. It is NOT possible to delete the 'About' section. 
There is currently no image on the 'About' page, although the Model is set up to be able to accept one. This is because
the site is a real world application, and the business owner may decide that they would like an image there in future. 
This would otherwise mean a lot of work for the developer.

#### Future Features:

In future I would like to add the following features:

- **Verified Purchases**: I would like to allow only customers who have bought an item to be able to leave a review for it. 
- **Custom Products**: I would like to be able to allow customers to be able to choose the fabric for their product from a selection on the site.
- **Wishlist**: I would like users to be able to create a wishlist.
- **Delivery Address**: I would like users to be able to specify different billing and delivery addresses.
- **Paypal**: I would like users to be able to pay for their items using Paypal.
- **Apple Pay**: I would like users to be able to pay for their items using Apple Pay.

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
- [Font Awesome](https://fontawesome.com/) was used for icons on the site.

## Information Architechture:

### Database Choice:

- SQLight was used in development, as it comes pre-installed with Django.
- PostgreSQL was used for the deployed site, as it is offered as an optional add-on by Heroku.

### Data Modeling:

- The image below was produced using the [Draw SQL app](#https://drawsql.app/)

<img src="static/readme_images/database_diagram.jpg">

## Accessibility:

### Alt Tags:

In order to ensure that all images are accessible for those using a screen reader, I have ensured that all images used 
throughout the site include alt tags.

## Testing:

Information about tests carried out can be found in a separate [testing.md](testing.md) file.

### Known Bugs and Fixes:

- On the edit product form, as well as the add product form, it is possible to set the 'quantity in pack' field to 0 or a negative integer. 
This is not ideal, and poor UX, but will be fixed in due course when I have more time and knowledge.

- There is a small amount of overflow on the navbar dropdown menus on the right of the screen on the smallest screens.
This will be fixed when I have more time.

- All successful messages are displayed on the same toast. It seems strange to have messages about product updates
with shopping basket items below them. When I have more knowledge, I will decouple these messages, so that they 
display separately.

- When adding or editing a product, the newly selected image is not displayed on the add_product/edit_product pages.
This is poor UX, as even though it is displayed on the product-detail page after the form has been submitted, 
it leaves the user wondering whether their image has been uploaded or not. I will fix this when I have the knowledge 
to do so.

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
It should look like this: 

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

9. Back on the main dashboard, click on 'deploy', and then under the 'Deployment' method section, select GitHub and 'Automatic Deploys'.
10. Ensure that in settings.py, the following code is commented out:
```
Database
 https://docs.djangoproject.com/en/3.1/ref/settings/#databases
```
and the at the following code is added:
```
DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
```
11. Make migrations using the following command:
```
python3 manage.py makemigrations
```
and migrate the database models to the Postgres database using the following command:
```
python3 manage.py migrate
```
12. Load the fixtures from the 'product_types.json' file and then from the 'products.json' file - which are contained in the 'fixtures' folder into the database. 
This is done by using the following command:
```
python3 manage.py loaddata <file name>
```
13. Create a new superuser with the following command:
```
python3 manage.py createsuperuser
```
and then enter chosen email, username and password.
14. In settings.py, contain the previously entered database setting in an if statement, and add an else condition, so that different databases are 
used depending on the environment.
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```
15. Disable 'COLLECTSTATIC' with the fillowing code: ``` heroku config:set DISABLE_COLLECTSTATIC=1 ``` 
so that Heroku doesn't attempt to collect the static files.
16. Add ```ALLOWED_HOSTS = ['downham-and-finch.herokuapp.com', 'localhost']``` to settings.py.
17. Add Stripe environment variables to settings.py.
18. Push to Heroku using the following command:
```git push heroku master```

### Amazon Web Services:

All Static and media files for the deployed version of the site are hosted in a Amazon Web Services(AWS) S3 bucket. 
In order to create your own bucket, please follow the instructions on the AWS website 
[Here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)

1. In the gitpod terminal, install boto3 and django-storages using the following commands:
```pip3 install boto3 ``` and ```pip3 install django-storages```
2. Freeze the new requirements into the 'requirements.txt' file using the ```pip3 freeze > requirements.txt``` command
3. Add 'storages' to INSTALLED_APPS in settings.py.
4. Add the following code to settings.py in order to link the AWS bucket to the website:
```
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'downham-and-finch'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
5. Create a custom_storages.py file in the root level of the project. Inside it, include the locations of the Static Storage and Media Storage.
6. Delete DISABLE_COLLECTSTATIC from the Heroku Config Variables.
7. Finally, push to GitHub, and all changes should be automatically pushed to Heroku too.

### Making a Local Clone:
In order to make a local clone of the Downham and Finch website, enter ```git clone https://github.com/Hgoatly/downham_and_finch.git``` into the
terminal. 

Alternatively, you can follow these steps, which are detailed on the official 
[GitHub Documentation](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)

Next, create an .env.py file in the root directory of the project, and add it to the .gitignore file. 
The following code needs to be added to the .env.py file:
```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<Your Secret Key>"
os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public Key>"    
os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret Key>"    
os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH Secret Key>"   
```

Then make sure that the required packages are installed by running the following command: 
```pip install -r requirements.txt```

Make migrations and then migrate in order to create a database, by running the following commands:
```python3 manage.py makemigrations``` and ```python3 manage.py migrate```.

Load the fixtures from the 'product_types.json' file and then from the 'products.json' file - which are contained in the 'fixtures' folder into the database. 
This is done by using the following command:
```
    python3 manage.py loaddata <file name> 
```

Create a superuser with the following command: ```python3 manage.py runserver``` and entering your credentials.

Run the app by entering the following command:
```python3 manage.py runserver```

## Credits:

### Code:

- **Code Institute Boutique Ado Project**: Much of this project was copied and adapted from the Code Institute 'Boutique Ado' project. Comments stating this have been added to the top
of files that have been copied and adapted in this way, as well as to views, as it was felt that by commenting on every piece of copied code 
would mean that the comments would detract from the code. If there is additional code that has been copied from Boutique Ado and NOT acknowledged in 
the corresponding file, then it is in error, and should have been acknowledged. 
- **Footer Element**: The footer element was copied and adapted from https://mdbootstrap.com/docs/standard/navigation/footer/.
- **Code Institute Slack Channels**: Slack was used extensively for debugging, and to bounce ideas off other students and CI staff members.

-**W3 Schools**: W3 Schools was referenced for debugging purposes.

### Images: 

- All face mask images are the property of Downham and Finch, and were taken from the Downham and Finch Etsy Page. As this project is a real world application
for the company 'Downham and Finch', doing this was within copyright guidelines.

- All pet bandana images that are not modelled by pets, are the property of Downham and Finch, and were taken from the Downham and Finch Etsy Page. As this project is a real world application
for the company 'Downham and Finch', doing this was within copyright guidelines.

- The pink and white pet bow tie image is the property of Downham and Finch, and was taken from the Downham and Finch Etsy Page. As this project is a real world application
for the company 'Downham and Finch', doing this was within copyright guidelines.

- All other product images (including the 'noimage' image) are from Shuttertock (I have a premium account).

- The background image on the homepage is from [Unsplash](https://unsplash.com/)

- The favicon image, is from [Flaticon](https://www.flaticon.com/)

- The favicon was generated by [Favicon cc](https://www.favicon.cc/)

### Content:

- All content on the site was either taken from the Downham and Finch Etsy and Facebook pages, or written by the developer.

## Acknowledgements:

- **My Mentor** Can Sücüllü, for help and guidance on this project.
- **My Friends and Family** for constant support, and feedback on the content and functionality.
- **Code Institute Slack Channel** for help answering my many questions.
- **Code Institute Tutor Support** for helping me work out why things weren't working how they should. In particular, Tim, Shirley, Scott, Igor and Jo for their kindness and patience. 


## Version Control: 

- Throughout the development process, regular commits have been made in Gitpod, which have been pushed to the Recipes Without Github repository.
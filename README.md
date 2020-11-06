[**jellett-gallery**](https://jellett-gallery.herokuapp.com/)

# **Jellett Gallery**

This site was created to fill a niche. There is no gallery in the country that exhibits female artists solely. Due to the disparities in public exposure for male and female artists, a female-focused space would seemimgly be dearly appreciated. This gallery is a space to promote young, upcoming female artists in the Ireland. The site was built/designed with that goal in mind. This project uses as its guide, the concept of a collectively administered gallery; where access between the collective should be equal, this is reflected in several design choices. 

[![Build Status](https://travis-ci.com/isntlee/Jellett_Gallery.svg?branch=master)](https://travis-ci.com/github/isntlee/Jellett_Gallery)
---

- [**Table of Contents:**](#table-of-contents)
    - [**UX**](#ux)
        - [**Project Goals**](#project-goals)
        - [**User Stories**](#user-stories)
        - [**Design**](#design)
        - [**Wireframes**](#wireframes)
    - [**Features**](#features)
        - [**Current Features**](#current-features)
        - [**Potential Improvements**](#potential-improvements)
    - [**Technologies**](#technologies)
        - [**Front-End**](#front-end)
        - [**Back-End**](#back-end)
    - [**Database Design**](#database-design)
        - [**Databases**](#databases)
        - [**Data Models**](#data-models)
    - [**Testing**](#testing)
        - [**Validators**](#validators)
        - [**Automated Testing**](#automated-testing)
        - [**Compatibility**](#compatibility)
        - [**User Testing**](#user-testing)
    - [**Deployment**](#deployment)
        - [**Local**](#local)
        - [**Remote**](#remote)
    - [**Credits**](#credits)
        - [**Coding**](#coding)
        - [**Content**](#content)
        - [**Special Thanks**](#special-thanks)

---

# UX

## Project Goals

The aim of this project is to sell/promote the work of the gallery's artists. The project will showcase their work as well as offering them for open bidding/purchase.  Non-registered users can browse the collection, add items to a bid, make a bid and make payments. Registered users will have these completed bids displayed in their  "My Account" page. Registered users are not expected to pay an extra fee for postage, however unregistred users are. The project has also included scope for superuser access, or for committe member access. The gallery is operated as a collective with group responsibilty, a committee member has the ability to add/edit/delete individual pieces from the gallery collection. This is to allow the members to fully control their own collections.

#### Target Audience Goals

-  To learn about the nation's finest upcoming artists
-  Be able to browse their work, and make bids/purchases
-  An easy to use layout and design that works on any device
-  Registered users should be able to view their account and order history

#### Client/Site Owner Goals

-  Promote the work of the gallery and the artists/committee members
-  Generate funds for the gallery/committee members through the bidding/purchase system
-  Allow artists/committee members control over their collection in a user-friendly means


## User Stories

"**As a visitor to the Jellett Gallery I expect/want...**"

1. To be able to easily find what I am looking for, I want the layout of the site to make sense so I am not confused or put off using it. 

1. The information I am presented with to be laid out in a way that is easy for me to navigate and digest, so that I find what I need quickly and efficiently.

1. The ability to search through small amounts of information to find what I need, and then be able to easily click to get more detailed information when I need it.

1. The site to be easily navigable from any device, desktop, tablet or phone. For the content to look good and be useable on all of these devices.

1. To learn more about the gallery and their artists, so that I can be assured I am bidding on a worthwhile piece. 

1. For all information and images to be laid out in a clear and easy to understand way, on whatever size screen I am viewing the website on.

1. Plenty of high quality images of the products for sale, so I have a clear idea of what I am buying and can see the quality of the products up close.

1. To be able to easily find out all the information I need to make an informed bid. I expect information about materials, measurements, and when in the artist's career they completed the work.

1. A text search function so that I can quickly narrow down my search when looking for something specific.

1. To be able to see a summary of my order on every page of the checkout process.

1. That once I am logged in I can access my account details and update them if I need to. 

1. To be able to find information easily on my past orders and how to cancel an order. 

1. To be able to easily get in contact with the gallery owners via their contact details.

1. Feedback from the website I am using when I interact with it, I expect pop-ups/toasts/messages to inform me when my forms have been completed and sent correctly. Or to let me know when an error has ocurred and what to do next.



## Design

#### Framework

- [Bootstrap 4.5.2](https://getbootstrap.com/)
    - Bootstrap is a framework for building front-end projects, created and designed by Twitter.
- [jQuery 3.5.1](https://jquery.com/y/)
    - jQuery, the classic choice, I decided to make this a crucial part of my scripts framework.

#### Aesthetic

The central ambition of the gallery is to promote the art. The aesthetic was chosen to make sure the images take centre stage. This is achieved by bold uncluttered text, and a central monochrome contrast. In an effort to instill a professional impression, the decision was made to limit the palette to the gallery conventions. 

- (#FAFAFA)(**off-white** - *central colour*)
- (#020202)(**off-black** - *contrast colour*)
- (#555555)(**light-grey** - *link colour*)
- (#33ADFF)(**light-blue** - *hover effect*)

#### Icons

- [Font Awesome](https://fontawesome.com/icons?d=gallery)
    - This is the leading icon set and toolkit, it is completely fit for purpose. 

#### Alerts

 - [Sweet Alerts](https://sweetalert.js.org/docs/)
    - I decided to apply this visually improved option for critical decisions such as deleting an artwork within collections management. 

### Wireframes

- The wireframes for this site were made with [draw.io](https://www.draw.io/), and accessible in the folder [wireframes](https://github.com/isntlee/sagacity/tree/master/wireframes)

-- 

# Features

## Current Features

### Artists

- The Artists link directs to the Artists page; here offering a list of the commitee/gallery members. The list is made of links that lead to the artist's collection.
    - There is a art display space on this page, which displays the artist's key piece when hovering over their name/link. 
    - The links open to the artist's personal page, containing biographical details and a list of pieces on sale/display at the gallery. 
    - These pieces can be bidded/purchased by first clicking on the title or image, that will lead the user to the artwork's detail page. Here the user is informed of the minimum offer/bid amount, and further details about the piece.
    - On the artwork detail page there is an "Add to Bid" button to allow purchase, this leads the piece being added to the cart/bag facility. Finally, committe members/superusers can edit or delete these piecesas there are buttons availiable on superuser status. 

### Accounts

**Register** 
- Found within the Accounts tab/icon:  Anyone can open/register a personal account. A username/password and email address is required. Email verification is in place and passwords are hashed to enhance security. 

**Login/Logout**
- Accounts tab/icon: For users with accounts, the sign-in procedure checks that the username/password matches the database record.  

**My Account** 
- Accounts tab/icon: This feature is open all registered users. It presents key user information, bidding/order history and an editable address form 

**Collections Management** 
- Accounts tab/icon: This feature is limited to commitee members/superusers. It allows these users to add pieces to the collection.  There are several required conditions to meet to add an entry such as name, description, offer/price, etc, etc.  

### Bag/Cart

- This icon leads to the bag/cart facility but referred to on the site as "Bid Details".
    - This is an opportunity to review the user's selection and remove any pieces from the bag/cart before bidding/purchase.
    - The icon displays on the navbar the number of items that are in the bag/cart.  
    - On selecting "Make Bid" the user is taken to the checkout facilty where purchase can be made. The page consists of a personal and billing details form, a summary of the bag/cart contents and payment form. Payment is currently made through the Stripe Online Payment Platform.
    - Unregisterd users are charged full delivery on their orders, while registered users are not charged at all. This feature is not mentioned on the site for several reasons; firstly, any attempt to offer "money off" might tarnish the gallery's reputation/brand and it was felt at commitee level that registering members/users should be encouraged but not blatantly.  
    - Successful payment leads to a confirmation page, that outlines the order's details in full and indicates that an email will be sent to the user's email address.

### Exhibitions/About Us Links

- These links lead to informative pages that are not interactive. They do have external informative links but that's the limit of their function. 

### Search

- Easily accessible search function, searches through the full collection based on title or description word-choice.
    - Sort-by function is present that organizes entries by set criteria whether the artist's name or the artwork's title.  

**Error Pages**
- There are two custom error pages for both 404 and 500 errors.



## Potential Improvements 

**Account Personalisation** 
- To build-in a series of additional options for the user after registering such as saving favourites, hiding personal entries that are still work-in-progress, undo entry deletes and an option to re-set passwords if lost. 

**Geo-location** 
- This would be a google map feature, that would indicate the location of important artistic centres in Ireland, especially Dublin. The user's personal location would update the map-centre as the page refreshed allowing real-time interaction. 

**Gallery app.**
- A gallery function within 'My Account' of the images of previous bid/orders.

**Rating system**
- With additional time, there would have been built a system to track whether a registered user had liked/voted for a piece or not, limiting that user to only ever adding one upvote or one downvote.

**Ranking system**
- This would exist on top of the Rating system allowing pieces to be displayed in artist's pags, and through search results, in terms of likes/votes. 

--

# Technologies

- [Gitpod](https://www.gitpod.io/) - Used as my IDE for coding.
- [GitHub](https://github.com/) - Used as remote storage of my code.
- [Stripe](https://stripe.com) - As payment platform to validate and accept credit card payments securely.
- [GIMP](https://www.gimp.org/) - Used for editing images.
- [TinyPNG](https://tinypng.com/) - Used to compress images for faster loading.

### Front-End

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used as the base for markup text.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
- [Javascript](https://www.javascript.com/) - Used as primary JavaScript functionality.
- [jQuery 3.5.0](https://code.jquery.com/jquery/) - Used as secondary JavaScript functionality.
- [Bootstrap 4.5.2](https://getbootstrap.com/) - Used as the overall design framework.

### Back-End

- **Django**
    - [Django 3.1.1](https://www.djangoproject.com/) - As python web framework for rapid development.
    - [Django Storages](https://django-storages.readthedocs.io/en/latest/) - A collection of custom storage backends with Django to work with boto3 and AWS S3.
    - [Gunicorn](https://pypi.org/project/gunicorn/) - WSGI HTTP Server for UNIX to aid in deployment of the Django project to Heroku.
- **Heroku**
    - [Heroku](https://www.heroku.com) - Used for the app hosting.
- **Python**    
    - [Python 3.8.5](https://www.python.org/) - Used as for back-end programming.
    - [Psycopg2](https://pypi.org/project/psycopg2/) - As PostgreSQL database adapter for Python.
    - [Pillow](https://pillow.readthedocs.io/en/stable/) - As python imaging library to aid in processing image files to store in database.
- **Databases**
    - [PostgreSQL](https://www.postgresql.org/) - For production database, provided by Heroku.
    - [SQlite3](https://www.sqlite.org/index.html) - For development database, provided by Django.


# Database Design:

## Databases:

- [PostgreSQL](https://www.postgresql.org/) - For production database, provided by Heroku.
- [SQlite3](https://www.sqlite.org/index.html) - For development database, provided by Django.


## Data Models:

**Users**

The User model utilized for this project is the standard one provided by **`django.contrib.auth.models`**

\
**OrderLineItem**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Order | order | on_delete=models.CASCADE | ForeignKey
Product | product | on_delete=models.CASCADE | ForeignKey
Quantity | date | default=1 | IntegerField
Lineitem Total | lineitem_total | max_digits=6 | DecimalField

\
**Category model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Name | name | max_length=100 | CharField
Friendly Name | friendly_name, blank=True | max_length=100 | CharField
Description | description | blank=True | TextField
Image Url | image_url | max_length=1024 | URLField
Image | image | blank=True | ImageField

\
**Order model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Order Number | order_number | max_length=32 | CharField
Username | user_profile | on_delete=models.SET_NULL, blank=True | ForeignKey
Date | date | auto_now_add=True | DateTimeField
Full Name | full_name | max_length=50 | CharField
Email | email | max_length=254 | EmailField
Phone Number | phone_number | max_length=20 | Charfield
Country | country | blank_label='Country *' | CountryField
Postcode | postcode | max_length=20, blank=True | Charfield
Town/City | town_or_city | max_length=40 | Charfield
Street Address 1 | street_address1 | max_length=80 | Charfield
Street Address 2 | street_address2 | max_length=80, blank=True | Charfield
County | county | max_length=80, blank=True | Charfield
Registered | is_registered | default=False | BooleanField
Delivery Cost | delivery_cost | max_digits=6 | Decimalfield
Order Total | order_total | max_digits=10 | Decimalfield 
Grand Total | grand_total | max_digits=6 | Decimalfield
Original Bag | original_bag | default='' | TextField
Stripe PID | stripe_pid | max_length=254 | Charfield

\
**Product model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Name | name | max_length=254 | CharField
Category | category | on_delete=models.SET_NULL | ForeignKey
Category Friendly | category_friendly, blank=True | max_length=254 | CharField
Sku | sku | max_length=254, blank=True | CharField
Description | description | blank=False | TextField
Dimensions | dimensions | max_length=12, blank=True | CharField
Year | year | max_length=1024, blank=True | IntegerField
Offer | offer | max_digits=6 | DecimalField
Image Url | image_url | max_length=1024 | URLField
Image | image | blank=True | ImageField


--

# Testing 

### Validators

**HTML**
- [W3C HTML Validator](https://validator.w3.org) - The code is valid. 

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - The code is valid. The only warnings concern imported items: AWS functions, and Bootstrap details. 

**JavaScript**
- [JShint](https://jshint.com/)
    - The code is valid, all undefined/unused variables are concerned with jQuery, Materialize and SweetAlert
    - The three undefined variables:
        '$' , 'M', 'swal' 
- [JSLint](https://jslint.com/)
    - For JS file, there are two warnings concerning unexpected use of terms with the search-bar code. These unexpected terms are both "for" as in those used in a "for" loop, this is not a serious concern.  
    - For jQuery, all the warnings are particularly minor and centre around undeclared/unexpected terms, the major warnings are about "$" or "document". This is not that helpful.   

**Python**
- [PEP8 Online](http://pep8online.com/)
    - All python files are all right.

### Automated Testing

- Tests were developed with the Unit testing framework, these tests were applied to the application's routes/forms; see the separate app tests folders. Unit-tests are run from CLI with the command: "python3 manage.py test"
- There are two varieties of tests: route/form tests watching clear behaviour and tests verifying actions. 
    - Behavior: testing routes/forms, asserting that all cases behave correctly and returning a request succeed status 200. 
    - Verify actions: the tests created concern writing/deleting from the database. 

#### Travis

- [Travis](https://travis-ci.org/) was used throughout the unit testing of this project to provide continuous integration with the deployed site. The [Travis Documentation](https://docs.travis-ci.com/) provides all the info needed to set it up.
- I set the heroku deployment settings for this project to only allow deployment when the travis had passed the latest push to the master branch on GitHub.

### Compatibility

**Mobile**
- Chrome Developer Tools, Android(Samsung A5/Galaxy S8) and Apple(Iphone 8) mobile phones used to test appearance of site and its various features. There are very minor differences between android/ios but all are cosmetic e.g. fonts displaying slightly differently, pages scrolling more fluidly or details being more immediately responsive on ios. 

**Desktop**
- Google Chrome, Microsoft Edge, Mozilla Firefox all work and display correctly, testing done on a local system. Testing of Safari has only been conducted on [BrowserStack](https://www.browserstack.com/), the site works correctly. 


### User Testing: 

Manual tests were carried out and the testing process was as follows:

**Landing Page**
 - Click "Jellett Gallery" and verified that home page appears.
 - Click on "Artists" button  - verified redirect to view "Artists" page.
 - Click on "Exhibitions" button  - verified redirect to view "Exhibitions" page.
 - Click on "About" button  - verified redirect to view "About" page.
 - Click on "Bag" icon  - verified redirect to view "Bid Details" page. If items have been added to bid, a number displays on the "Bag" icon. 
 - If user is logged-in; “My Account” is displayed in the dropdown menu after clicking the account icon and clicking this link brings you to the "My Account" page.
 - If user is not logged-in; "Register" and “Login” isdisplayed in the dropdown menu after clicking the account icon and clicking either link will bring you to that page.
 - Search Button - click to open search bar. 

###### Register/Sign-Up Page
- Verify that clicking on the link brings user to the registration page. 
- All five fields required for registration are displayed. 
- Verify that username and email must be unique - message appears if details are not unique.
- Verify that password must be unique - message appears if password is too common, short or too similar to username.
- Tested registering successfully by varifying email address and was returned to the homepage.

###### Login/Sign-In Page
- Verified that the login link directs to the login page
- If user enters an incorrect set of details, the error message will fire. 
- If user enters the correct login details they are returned to the homepage. 

###### Logout
- Verified that the user is returned to home and logged out.

###### My Account Page (Profile)
- Verified that the user details are present. 
- If bids/orders have been made then order details visible. 
- If bids/orders have been made then billing details visible. 
- Verifed that billing details presented in all seven form fields and that these details are editable. 

###### Artists Page
- Confirm that on hovering over Artist list/links that display box changes image, and link changes colour. 
- Verified that by clicking all links, all lead to the Artist's personal collection page.

###### Artists Collection Page (Products)
- Verified that the artists's personal image and introduction is present 
- Confirmed that all nine artworks are displayed and all links to artwork detail pages are active/functional.

###### Artwork Detail Page (Product Detail)
- Verified that the artwork image and details are present. 
- Confirmed that the "Keep Browsing" button is functional, and returns to artist's collection page. 
- Confirmed that the "Add to Bid" button is functional, leads to number increasing on cart icon and message appears "Added ..... to your bid"

###### Bid Details Page (Bag/Cart)
- Verified that if item in bag/cart, it is visible on page as image, title, artist and offer/price.
- Confirmed that any totals for items are correct. 
- Confirmed that clicking "Click here to remove" does in fact remove item.
- Confirmed that  "Keep Browsing" and "Make Bid " buttons both work, directing user to appropriate destination.

###### Your Bid Page (Checkout)
- Verified that item/items are visible on page as image, title and offer/price.
- Confirmed that all totals whether postage included or not are correct.  
- Confirmed that all forms present are functional. 
- Verified that user details present, and if previously ordered then postage address details also present. 
- Confirmed that test credit card number "4242 4242 4242 4242", Exp: 04/24. Security no: 242. Postcode: 42424; lead to a successful payment. 

###### Thank You Page (Checkout - Success)
- Verified that page opens after successful test payment  and that message of same is visible. 
- Confirmed that there is a novel order number in place, and that all form fields are filled.  
- Confirmed that unregistered users pay full postage while registered users do not.
- Verified that "Return to Collection" button does return user to Artists page.

###### Search
- Enter a term into the search form and confirm that the correct results are returned. 
- Verified that sort-by function operates correctly. 

###### Committee Member Access (SuperUser)
- Verified that the option "Collections" is now availiable, and that this link leads to the Collections Management Page. 
- On the Collection Management Page, verifed that all nine form fields are availiable and that the image select function operates. 
- Confirmed that added pieces/items are added to the relevant collection and are searchable. 
- On the Artwork Detail page, that the options edit and delete are visible/functional.
- Confirmed that on selecting edit, superuser led to edit page which has all nine active form fields and that the image select function operates.
- Confirmed that edited pieces/items are added to the relevant collection and are searchable. 
- Confirmed that on selecting delete, an alert is fired requiring another click to proceed. 

--

## Deployment

#### Source control and deployment was carried out primarilly via [GitHub](https://github.com/isntlee/Jellett_Gallery) and [Heroku](https://jellett-gallery.herokuapp.com/)

### Local Deployment

Do ensure that you have an IDE such as 
- [Gitpod](https://www.gitpod.io/)

Please note - in order to run this project locally on your own system, you will need the following installed:
- [Python3](https://www.python.org/) to run the application.
- [PIP](https://pip.pypa.io/en/stable/) to install app requirements.
- [GIT](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for version control.

To access full functionality on the site locally, you will need to create accounts with the following services:
    - [Stripe](https://dashboard.stripe.com/register)
    - [AWS](https://aws.amazon.com/) and [set up an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)


### Instructions 
1. Clone the Jellett Gallery repository by either downloading from here or type the following command into your terminal:
    ```
    git clone https://github.com/isntlee/Jellett_Gallery
    ```
2. Navigate to this folder in your terminal.

3. A virtual environment is recommended for the Python interpreter. Enter the command:
    ```
    python3 -m .venv venv
    ```  
 - _Warning : **This Python command may differ** depending on operating system, the command required could be **python** or **py**_

4. Initialize the environment by using the following command: 
    ```
    .venv\bin\activate 
    ```
 - _Warning : **This command may differ** depending on your operating system_

5. Install all the requirements and dependancies with the command 
    ```
    pip3 -r requirements.txt.
    ```
6. Within your IDE create a file where you can store your sensitive information for the app, I would advise an env.py file.
    ```
    import os
    os.environ.setdefault("STRIPE_PUBLISHABLE", "your_stripe_publishable_key")
    os.environ.setdefault("STRIPE_SECRET", "your_stripe_secret_key")
    os.environ.setdefault("SECRET_KEY", "your_django_secret_key")
    ```
7. If you have restarted your machine to activate your environment variables, do not forget to reactivate your virtual environment with the command used at step 4.

8. Migrate the admin panel models to create your database template with the terminal command
    ```
    python3 manage.py migrate
    ```
9. Create your superuser to access the django admin panel and database with the following command, and then follow the steps to add your admin username and password:
    ```
    python3 manage.py createsuperuser
    ```
10. You can now run the program locally with the following command: 
    ```
    python3 manage.py runserver
    ```
11. Once the program is running, go to the local link provided and add `/admin` to the end of the url. Here log in with your superuser account.



### Remote Deployment

This site is currently deployed here on [**Heroku**](https://jellett-gallery.herokuapp.com/) using the **master** branch on GitHub. To implement this project on Heroku, the following steps were taken:

### Instructions

1. Create a `requirements.txt` file using the terminal command `pip3 freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps).

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
--- | ---
AWS_ACCESS_KEY_ID | `<your secret key>`
AWS_SECRET_ACCESS_KEY | `<your secret key>`
AWS_STORAGE_BUCKET_NAME | `<your AWS S3 bucket name>`
DATABASE_URL | `<your postgres database url>`
SECRET_KEY | `<your secret key>`
STRIPE_PUBLISHABLE | `<your secret key>`
STRIPE_SECRET | `<your secret key>`

8. From the command line of your local IDE:
    - Enter the heroku postres shell 
    - Migrate the database models 
    - Create your superuser account in your new database

9. In your heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch".

10. Once the build is complete, click the "View app" button provided.


## Credits: 

### Coding

- [Materialize](https://www.youtube.com/watch?v=gCZ3y6mQpW0&list=PL4cUxeGkcC9gGrbtvASEZSlFEYBnPkmff)
- [GoogleMaps JSON objects](https://www.youtube.com/watch?v=mfjqLmD6Li8)
- [GoogleMaps API](https://www.youtube.com/watch?v=pFpBibg6nac)
- [Pagination Flask/MongoDB](https://www.youtube.com/watch?v=Lnt6JqtzM7I)
- [Pagination Flask/MYSQL](https://www.youtube.com/watch?v=PSWf2TjTGNY)
- [Unit-testing](https://www.youtube.com/watch?v=6tNS--WetLI)
- [Text Indexing](https://www.youtube.com/watch?v=dTN8cBDEG_Q)
- [Password Hashing](https://www.youtube.com/watch?v=jJ4awOToB6k)
- [Flask](https://www.youtube.com/watch?v=bLA6eBGN-_0)
- [Flash messages](https://www.youtube.com/watch?v=lcVdZtVvnnk)

### Content 

- [Google Images](https://images.google.com/) 
    - All images taken from Google Image searches. 
- [Favicon.io](https://favicon.io/) 
    - Designed and produced flavicon 

### Special Thanks

- [Precious Ijege](https://github.com/precious-ijege) 
    - My Code Institute mentor
- [Corey Schafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) 
    - His tutorials have been essential research for many.

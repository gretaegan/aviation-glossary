# Aviation Glossary

! mock up will go here 

## Introduction

Welcome to Aviation Glossary. 
This was created for my third project as part of the Code Institute, Full Stack software development course. 
Aviation Glossary, is a full-stack site, allowing users to share their own data with the community, and benefit from having convenient access to the data provided by all other users.
The goal of Aviation Glossary is showcasing my knowledge of Python and the Flask framework. MongoDB is used to manage the database. HTML, CSS, and JavaScript are also used in this project. 
Finally, I would like to thank you for visiting Aviation Glossary,  A link to Aviation Glossary can be found below.

[Aviation Glossary live site](https://aviation-glossary.herokuapp.com/)


# UXD - User Experience Design

The design and development for Aviation Glossary was based on Jason James Garrets, “The Elements of User-Experience”. The 5 different planes used to design and develop Aviation Glossary are, 
	The Strategy Plane
	The Scope Plane
	The Structure Plane
	The Skeleton Plane
	The surface Plane. 

## The Stragety Plane 

The Strategy Plane is where the research for this project took place. Using research from visiting similar projects and discussing concepts with other people I came up with user and creator goals. The goals will allow me to stay focused on keeping the User at the forefront during the development while allowing me to fulfil my goals as the creator.

### User Stories 

#### Annonymous User

| **As an anonoumous I would like to ** : |  **So that I can**  : |
| ------------- |:-------------:|
| easily understand the main purpose of the site | determine if it is what I need |
| use an aesthetically pleasing site| enjoy my user experience |
| easily navigate the site| quickly find what I need |
| find information is clearly presented | absorb it with minimal effort |
| have features load quickly | save time |
| view the site on different screen sizes| use it on a desktop or on the go |
| view/search words and definitions | expand my knowledge of aviation terminology |

#### Registered User

A registered users goals are in addition to the above mentioned user goals.

| **As a registered user I would like to ** : |  **So that I can**  : |
| ------------- |:-------------:|
| upload my own definitions or words | share my knowledge with the community |
| edit and delete content I have provided | manage my definitions over time |
| login to a secure profile account | view and manage my uploads in one location |

### Creator Goals 

As the creator of this site, my goal is to provide a community for fellow aviation lovers to learn more about the kind of phraseology we use in the sky. 
I want the site to be useful and informative to both experienced aviators, and people with no background, but an interest in aviation.


## The Scope Plane 

The Scope Plane is where I focused on my features of Aviation Glossary.
To avoid falling into a trap of flooding the project with multiple features that may hinder the development, due to deadlines and my current knowledge I focused on releasing Aviation glossary in phases. 

Phase 1 would be release as a minimal viable product, providing users with necessary features that allow them to interact with the site, share and view data, while keeping the design simple while still providing a positive emotional response to the user. 

Phase 2 would allow to me to build on the feedback I receive. Fixing any issues that may have been overlooked and adding additional features that would further enhance the user experience. 

#### Phase 1 Features

The site is currently in Phase 1 stage and features:

- Responsive Design
- Informative homepage 
- Sticky top and responsive Navbar 
- MongoDB database to store all data
- CRUD functionality - to add/ edit and delete definitions from the Glossary
- Login/Logout functionality
- User dashboard
- Search functionality

#### Phase 2 Features

Phase 2 would feature:

- Additional interactive features.
- Pagination so that the Glossary page would be limited per page as the site and glossary grows bigger.
- Account page so that users could change their username or password.
- A fact-checker system to ensure that wrong definitions were not allowed to be added to the glossary.

Phase 1 will act as the project's minimal viable product, offering users simple CRUD functions. While still meeting the goals for first-time and regular users.

Phase 2 will build further on the project adding features that will further provide user functionality and improve the user experience.


## The Structure Plane 

#### Features 

* Images 

Imagery used in this project are relevant to the brand and exciting. The homepage features a Bootstrap Carousel with three photos: an Aer Lingus A321 performing a steep turn,
a lit-up runway on the final approach to land, and a Cathay Pacific Boeing 747 on approach into (now defunct) Kai Tak airport, Hong Kong. 
The hero image is of an aircraft lining up on a lit up runway at dusk. 
These images were chosen because they are relatable to the content on the page, and add a touch of excitement to the site. 
I intend this project to be used by people who love aviation, so these pictures cater to my audience. 

* Colors

My project focuses on a simple, clean color palatte consisting of:

- #12d6f8 and hsl(189, 96%, 67%) (bright blues)

- #021752  (navy)

and 

- #9bd3dd  (duck egg blue)

The hero image has a black gradient overlay to help the text stand out more and to tone down the bright lights in it. 
The navy color (#021752) used for the Navbar and Footer, provides a calm and professional feel to the site and the lighter blues stand out well over it.

* Typography

The font used in this project is 'Raleway' from Google Fonts. 
Raleway is used at different font weights and letter spacing throughput the project, to add emphasis to important headings such as the hero image text and the glossary.
Text is consistent across all pages and is centered. 

* Overall Design 

It is important to me that the site looks professional, simple and without anything too gimmicky. I have kept the design reletively simple across all pages, on the 
log in, register, user dashboard and glossary pages I have used a simple banner to add to the look of the site. The banner is a blue background featuring 
the engine and wing of an aircraft. 

 
#### Database Design 

The database is separated into 3 collections:
- Users
- Definitions
- Categories

Users sign up with a username and password which is saved in MongoDB with a unique identifier number.

Definitions hold the category name that it comes under, the definition itself, and the user who created it.

Categories are the what the definitions can fall under. I have used 3:

- Meteorology (weather and climate related abbreviations)
- RT (Radio Telephony - how pilots and ATC speak over the radios)
- General (anything else can fall under general- airport terminology, instrumentation, etc)

*Users*
```
{
    "_id": {
        ObjectId: "60b603b2718df5f505166634"
    },
    "username": "greta1",
    "password": "users password here 
}
```

*Definitions*
```
{
    "_id": {
        ObjectId: "60ba321013fa9863d7d52d14"
    },
    "category_name": "Meteorology",
    "definition_name": "METAR",
    "definition_description": "Aviation Routine Weather Report. Meteorological Aerodrome Report",
    "created_by": "gretaegan"
}
```

*Categories*
```
{
    "_id": {
        ObjectId: "60ab8905b902271d7fbd663d"
    },
    "category_name": "RT"
}
{
    "_id": {
        "ObjectId: "60ab8931b902271d7fbd663e"
    },
    "category_name": "Meteorology"
}
{
    "_id": {
        ObjectId: "60ab897ab902271d7fbd663f"
    },
    "category_name": "General"
}
```

#### Security 

During development sensitive data, such as database configuration variables, were saved in an env.py file. This file is not uploaded to GitHub for security purposes. These details are stored on Heroku once the site has reached the deployment stage.

The users accounts are protected with password hashing avaialble via Werkzeug.

### Future Features 

At the moment, this project is limited by my own lack of experience with Python, and time constrainsts due to needing to reach a deadline to submit.
Once I have become more competant with Python and have more time on my side, I would like to implement the following features:

- An option to change users username and password if they should want to.
- A feature to prevent duplicate definitions being uploaded.
- A feature to stop incorrect definitions being uploaded.


## The Skeleton Plane 

Figma was used to create the wireframes for this project and they can be found 

discus changes from your project.

## The Surface Plane 

Features included in this project :

- Navbar which is responsive across all screen sizes. I used Bootstrap for this. On smaller screens, the navbar is hidden and a hamburger menu is shown instead.
  The Navbar brand acts as another link back to the homepage.
- Footer section has social media icons which open the corresponding website in a separate tab.
- Hero image with a dark overlay to help the text stand out. Image is consistent with the project theme.
- A carousel of images and sample definitions from the glossary. The images are relevant to the project and exciting to look at.
- Flash texts provide the user with constant feedback throughout the project. 
- Users can create an account which will enable them to add their own definitions into the glossary. Users can edit or delete these definitions if they decide to.
- Search functionality is added to the glossary, users can search for a keyword or definition and reset the search once they are finished.
- A modal shows if the user decides against deleting their post, to ensure they have a chance to cancel the request.
- User input forms use defensive programming, providing feedback if the form is correctly submit.

Features left to implement:

- Further interactive elements to make the site more interesting.
- Pagination on the glossary as it grows, to prevent it becoming too long.
- An element to prevent incorrect definitions or words being added to the glossary.

# Technologies Used

- [Python](https://www.python.org/)
    - The core main language used on the project, all functionality to run and view this project was built    with Python.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    - Used as the templating language with Python.
- [Heroku](https://www.heroku.com/)
    - Used as the deployment source for this project.
- [MongoDB](https://www.mongodb.com/2)
    - Used as document based datebase for this project.
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
    - Used as the basic building block for the project and to structure the content.
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
    - Used to style all the web content across the project. 
- [Bootstrap](https://getbootstrap.com/)
    - Used as the main framework to make the project responsive.
- [jQuery](https://jquery.com/)
    - Used with Bootstrap to make the navbar responsive.
- [JavaScript](https://www.javascript.com/)
    - Used for the bootstrap navbar for extending collapse plugin to implement responsive behavior, Text shadow animation added on hero image text to add a subtle red text shadow when pages load.
- [Google Fonts](https://fonts.google.com/)
    - Used to obtain the fonts linked in the header, fonts used were Roboto and Dancing Script
- [Font Awesome](https://fontawesome.com/)
    - Used to obtain the social media icons used in the footer.
- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
    - Used as a primary method of fixing spacing issues, finding bugs, and testing responsiveness across the project.
- [Github](https://github.com/)
    - Used to store code for the project after being pushed.
- [Git](https://git-scm.com/)
    - Used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [Gitpod](https://www.gitpod.io/)
    - Used as the development enviroment.
- [Figma](https://figma.com/)
    - Used to create the wireframes for the project.
- [AutoPrefixer](https://autoprefixer.github.io/)
    - Used to parse my CSS and add vendor prefixes.


# Testing

The following testing has been done on this project:
- User Story Testing
- Lighthouse Performance Testing
- CRUD Functionality Testing
- Project Input Field Testing
- HTML / CSS / JavaScript / Python all checked with validators.

### User Story Testing 

 | **Annonymous User Goals ** : |  ** Supporting Features**  : | **Outcome** : |
| ------------- |:-------------:|
| easily understand the main purpose of the site | Homepage has an aviation related image and informative text  | PASS |
| use an aesthetically pleasing site| Design is consistent and fitting with the theme, colors are pleasant and calm | PASS |
| easily navigate the site| Navbar is clearly labeled and promotes easy naviation of the site | PASS |
| find information is clearly presented | All text is displayed clearly and in a straightforward manner | PASS |
| have features load quickly | All features load quickly with a standard internet connection | PASS |
| view/search words and definitions | The glossary is simple and informative and shows all definitions in a list | PASS |


| **As a registered user I would like to ** : |  **In addition to the above goals**  : | **Outcome** : |
| ------------- |:-------------:|
| upload my own definitions or words | Users can add their own words once signed up and view in the glossary | PASS |
| edit and delete content I have provided | Users can see edit/delete buttons for their own definitions and they function as intended | PASS |
| login to a secure profile account | Users have their own dashboard where they can easily navigate the site | PASS |


### CRUD Functionality Testing 

To test database functionality for the project:

- Create a new User account.
- Check new user appears in user collection in MongoDB.
  If after creating an account I am signed in, I will sign out and try to log back in to check for any errors.
- Create a definition and add it to the glossary.
- Check to see if the post correctly appears in the posts collection in MongoDB.
   Edit the post.
- Check to see if the post is correctly edited in the posts collection in MongoDB.
   Delete the post.
- Check to see if the post is correctly removed from posts collection in MongoDB.


A link to a PDF of my sample testing can be found [Here](link will go here)

### Project Input Field Testing 

- Input fields correctly restrict user input when maximum/minimum character count is met.
- Input fields correctly display an error if user attempts to you special charcaters.


### Lighthouse Performance 

### Code Validators

- HTML results can be found [here]()

-CSS results cam be found [here](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Faviation-glossary.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
 The CSS validator returned a number of errors and warnings however they are all from Bootstrap and Font Awesome and none from my own code.


- Javascript was run through JSHint.com and returned no issues.


### Further Testing 

The following browsers were used to test the project:

- Google Chrome
- Mozilla Firefox
- Microsoft Edge The project passed all tests on the browsers listed above.
- Google Chrome Developer tools was used to test the resposiveness of the project on the following emulated devices:

Apple Ipad
Apple Ipad Pro
Microsoft Surface Duo
Iphone 5/SE
Iphone 6/7/8
Iphone 6/7/8 PLUS
Iphone X

Real world testing was done on my own laptop and phone:

- Dell G7 17.3" Full HD 144Hz
- iPhone 11


### Known Bugs and Fixes

- The hero image on the homepage does not fully fit the screen, leaving a small amount of whitespace on either side.
  I have identified the issue in Chrome Dev Tools:
     - Padding-right: var(bs gutter x, .75rem)
     - Padding-left: var (bs gutter x, .75rem)

- When a user tried to edit a definition their was no value in the definition field that appeared in the glossary.
  This was due to a mismatch of input id's on the form, which has since been fixed.

- Edit and Delete buttons were showing, in the glossary, for all users who were not logged in. It is intended that only users who created a definition would be able
  to see and use these buttons. This was fixed by adding a "created_by": to all documents in the database and ensuring that all had a value.



# **Deployment** # 

The master branch of this repository is the most current version and has been used for the deployed version of the site.
The Code Institiue student template was used to create this project. 
[Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)
- Click the *Use This Template* button.
- Give your repository a name, and description if you wish.
- Click the *Create Repository from Template* to create your repository. 
- Click the *Gitpod* button to create a gitpod workspace, this can take a few minutes.
- When working on project using Gitpod, please open the workspace from Gitpod, this will open your previous workspace rather than creating a new one.
Use the following commands to commit your work, 
- `git add . ` - adds all modified files to a staging area.
- `git commit -m "A short message exlaining your commit"` - commits all changes to a local repository.
- `git push` - pushes all your commited changes to your Github repository.
**Creating an Application with Heroku,**
- Goto [Heroku.com](https://www.heroku.com/) and create an account or login. 
- Click the *New* dropdown and select *Create New App*.
- Enter a name for the project.
- Select your region.
**Connecting your Heroku account to your Github Repository,**
- Click on *Deploy* tab and choose `Github-Connect to Github`.
- Enter the GitHub repository name and click on *Search*.
- Once the correct repository is found, click on *Connect*.
**Setting you Enviroment Variables**
- In the *Settings* tab, click on *Reveal Config Vars* and set the following variables,
- IP : 0.0.0.0
- PORT : 5000
- MONGO_DBNAME : *Your MongoDB database name*
- MONGO_URI :  *This can be found on MongoDB, goto to clusters -> connect -> connect to your application*
    - Please remember to update the URI with your database name and password.
- SECRET_KEY : *This is a custom key of your choosing to keep sessions secure* 
**PLEASE NOTE TO SUCCESFULLY DEPLOY WITH HEROKU, YOUR PROJECT MUST HAVE A *requirements.txt*  and *Procfile* files.**
The following commands in the Gitpod CLI will create the relevant files.
`pip3 freeze --local > requirements.txt`
`echo web: python app.py > Procfile`
**Running this Project Locally**
**You will need create a env.py file, which contains all the enviroment variables you used on Heroku, Please note this file should be added to a .gitignore file to prevent the file from being commited.** 
THESE DETAILS SHOULD BE PRIVATE AND SHOULD NOT BE DISCLOSED FOR SECURITY PURPOSES!
- Navigate to the Github repository. 
- Click the *Code*.
- If you choose to download the zip file, you can unpackage this in Gitpod.
- If you choose to copy the Git URL, please continue to follow the steps below.
- In Gitpod, in the CLI type `git clone "Git URL"`.
- This will now create a clone of the project on your machine. 
Once the project has been loaded please run the following command in the CLI to install the project required packages, 
`pip install -r requirements.txt`
**Creating a Fork of the Project in your Github Repositories**
- Head over to the Github Repository.
- In the top right, just under your profile you have a "Fork" button.
- Clicking the "Fork" button will create a copy of the project in your repository.


# Credits 

- Code Institute. The backend section of my project was built upon the Mini-project walkthrough project. I relied on this to create my own 
   backend section.

- Bootstrap. I referenced the Bootstrap documents often thoughout my project, and used it to create the Carousel, Forms, Modal, layout and responsive Navbar.

- Media. Images were taken from:
  reference here 

- Content. Content from the gallery was taken from Skybrary.aero and my own knowledge from flight school. 


# Acknowledgments

- Oluwafemi Medale, my mentor who has provided me with so much help and from whom I have learned so much. I would not have gotten this far in the course without him.

- Code Institute Tutor team. The tutor team, with special thanks to Jo, have helped me to find solutions to issues I had with the project and were always super kind.

- Captain Andy O'Shea and the rest of the Airline Pilot Club, for providing me with invaluably useful content for the glossary, and lots of encouragement to create the project.

- Harry Dhillon, for always being the person I always turn to when I am struggling, always going above and beyond to help, and always offering encouragement.
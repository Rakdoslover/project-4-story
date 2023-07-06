# The Lonely Beach Project

## Description

This site hosts a story involving it's users.
Each week the author posts a story chapter without a title and placeholder
picture, the users may propose a title and a picture for this weeks chapter.
By the end of the week the author picks the one he/she likes the most and
renames the chapter and updates the picture accordingly.

### **[Live Site](https://the-lonely-beach-project-aff864383002.herokuapp.com/)**

---

### **[Repository](https://github.com/Rakdoslover/project-4-story)**

---
## Table of contents
<a name="tcontents">Back to Top</a>
 1. [ UX ](#ux)
 2. [ User Stories ](#userstories)
 3. [ Features ](#features)
 4. [ Technology Used ](#tech)  
 5. [ Testing ](#testing)   
 6. [ Screenshots ](#screenshots) 
 7. [ Future Implemetations ](#future)  
 8. [ Content ](#content)  
 9. [ Credits](#credits) 
 10. [ Acknowledgements](#acknowledgements)

## UX
<a name="ux"></a>

![Lucid Chart](/media/pictures/database-structure.jpg)

### Database 
#### AllAuth User

| id | Field |
|--|--|
| User |OneToOneField  |
| Username |Charfield|
|email|EmailField|
|Password|Charfield|

---

#### Chapter Model

| id | Field |
|--|--|
|Title|Charfield|
|Slug|Slugfield|
|Author|Foreignkey|
|Featured Image|Cloudinary image|
|Excerpt|TextField|
|Updated on|DateTimeField|
|Content|TextField|
|Created on|Datefield|
|Status|IntegerField|

---

#### Comment Model

| id | Field |
|--|--|
|ID|BigAutoField|
|User|Foreignkey|
|Post|ForeignKey|
|Name|CharField|
|Proposed Title|CharField|
|Email|EmailField|
|Body|TextField|
|Created on|DateTimeField|
|Approved|BooleanField|
|Featured Image|CloudinaryField|

[Back to Top of page](#tcontents)

---

## User Stories and Project
<a name="userstories"></a>

### Goal
---
The main goal for this project is to create a user friendly site with a simple
authentication login/signup and a place interactive storytelling platform.
Users are supposed to read the chapters published and dependeing on the theme of
the story post a comment with a proposed title and a featured image with connections
to the them of the text.
The comments are, if you're authorized and logged in, CRUD friendly.

### Agile Project
---
This project was started alongside a GitHub Projects Page to track issues that I had to solve further on.
The initial aim was to track steps and features needed to get the functionallity and layout as per project goal. 
I wrote epics with different themes according to what the user/admin/author wanted
to be able to do.

---
To see Kanban please click [here](https://github.com/users/Rakdoslover/projects/5/views/1)

I recognized 7 epics that would make the site work in the way I wanted and needed.
I also got 1 story I would like to have implemented but couldn't find time for.

For these 7, I made issues through the "project 4 story" Project on repository.
The plan was to make them all at first and cross them out as the project progressed,
but at times I got stuck on problems not forseen, which caused me to cross them off
a little more haphazardly.

#### User stories

Down below you can find both the fulfilled stories but also those not completed.

##### Completed

1. [USER STORY: Create Account](https://github.com/Rakdoslover/project-4-story/issues/1)
2. [USER STORY: Admin Page](https://github.com/Rakdoslover/project-4-story/issues/2)
3. [USER STORY: Site Pagination](https://github.com/Rakdoslover/project-4-story/issues/3)
4. [USER STORY: Create Comment](https://github.com/Rakdoslover/project-4-story/issues/4)
5. [USER STORY: Deploy the Site](https://github.com/Rakdoslover/project-4-story/issues/5)
6. [USER STORY: UD Comments](https://github.com/Rakdoslover/project-4-story/issues/6)
7. [USER STORY: View Comments](https://github.com/Rakdoslover/project-4-story/issues/7)

##### Uncompleted

1. [USER STORY: Rate Comments](https://github.com/Rakdoslover/project-4-story/issues/8)

[Back to Top of page](#tcontents)

---

## Features
<a name="features"></a>

#### Users can:

- **Users can** create an account (**Create**)
- **Users can** log into their account
- **Users can** log out of their account
- **Users can** create comment on chapter **(Create)**
- **Users can** read comments from other members *(**Read**)
- **Users can** view chapters from home page (**Read**)
- **Users can** edit their own comments (**Update**)
- **Users can** delete their own comments (**Delete**)
- **Users can** edit and delete others comments/chapters if they have superuser status through the adminpanel (**Update/Delete**)

#### User cannot:

- **Users cannot** post comments without an account or being logged in.
- **Users cannot** edit comments they've made previously without being logged in.
- **Users cannot** access the admin panel of the website unless they have admin status.
- **Users cannot** 

#### Website Features

##### Chapters on Home page

- Chapters are published in order of newest to oldest so that it's easy for members to find the newest chapter in the story.
- Chapters are paginated to a maximum of 6 per side to not fill up the whole screen with chapters.
- User are able to get a small excerpt of what the theme of the chapter is.

##### Chapter Detail page

- Users are able to read the published chapter on a separate page than the home screen.
- Users are able to comment, if authorized, and participate in the stories community.
- users can use CRUD to change what they already commented or delete it completely.

[Back to Top of page](#tcontents)

---


##  Technology Used
<a name="tech"></a>

---

### Html

 - Used to structure my webpages and the base templating language.

### CSS

 - Custom CSS was written on bits to make it stick out but played a background role over functionality.

### Python

 -  Used for the logic in this project.

### Django

 -  Framework used to build this project. Provides a ready installed admin panel and includes many helper template tags that make writing code quick and efficient.

### Bootstrap 5
 - Used as the base front end framework to work alongside Django.

### Allauth
 - To implement quick and easy user registration and login, modified after implemetations

### GitHub
 - Used to store the code for this project & for the projects Kanban board used to complete it.

### Heroku
- Used to host and deploy this project.

### ElephanSQL
- Heroku PostgreSQL was used as the database for this project during development and in production.

### Cloudinary
- Used to host the static files for this project including users featured images.

### Git
- Used for version control throughout the project and to ensure a good clean record of work done was maintained.

### Lucidcharts
- Used for to visulize the database structure


[Back to Top of page](#tcontents)

---

## Testing
<a name="testing"></a>


### Main Site Testing
**TESTING** | **ACTION** | **EXPECTATION** | **RESULT**
----------|----------|----------|----------
Home Page   | Size to 320px using Chrome Dev Tools | Elements look good @ 320px | Works as expected
Home Page	| Size to 1920px using Chrome Dev Tools | Elements look good @ 1920px | Works as expected
Login form | Click "Signin" button without data in form fields | Cannot submit form | Works as expected
Logout form | Click "Signout" button | Submits form and logs out user | Works as expected
Signup form | Click "Signup" button without data in form fields | Cannot submit form | Works as expected
Nav bar - home page | Click home button | Home button takes me to the home page | Works as expected
Nav bar - register page | Click register button | Register button takes me to the signup page | Works as expected
Nav bar - login page | Click login button | Login button takes me to the signin page | Works as expected
Nav bar - logout page | Click logout button | Logout button takes me to the signout page | Works as expected
Chapter Page   | Size to 320px using Chrome Dev Tools | Elements look good @ 320px | Works as expected
Chapter Page   | Size to 1920px using Chrome Dev Tools | Elements look good @ 1920px | Works as expected
Login Page   | Size to 320px using Chrome Dev Tools | Elements look good @ 320px | Works as expected
Login Page   | Size to 1920px using Chrome Dev Tools | Elements look good @ 1920px | Works as expected
Signup Page   | Size to 320px using Chrome Dev Tools | Elements look good @ 320px | Works as expected
Signup Page   | Size to 1920px using Chrome Dev Tools | Elements look good @ 1920px | Works as expected
Logout Page   | Size to 320px using Chrome Dev Tools | Elements look good @ 320px | Works as expected
Logout Page   | Size to 1920px using Chrome Dev Tools | Elements look good @ 1920px | Works as expected

### Account Registration
| Test | Result |
|--|--|
| User can create account |Pass|
| User can log into account |Pass|
| User can log out of account |Pass|

---

### Chapter and Pagination 
| Test | Result |
|--|--|
| User can open each chapter paginated on the site |Pass|
| User can go back and forth between sites with Next/Prev-button |Pass|
| User can see chapters without being logged in |Pass|

---

### Nav Bar
| Test | Result |
|--|--|
| Users can engage with the nav bar on the home page | Pass |
| Users can engage with the nav bar on each of the login/logout/signup pages | Pass |
| Users can engage with the nav bar on the chapter detail page | Pass |

---

### Create Comment and Read Comments
| Test | Result |
|--|--|
| Authorized users can comment on a specific chapter | Pass |
| All users can read comments posted by authorized users | Pass |

---

### Update Comment and Delete Comment
| Test | Result |
|--|--|
| Authorized users can update a previously published comment they own | Pass |
| Authorized users can delete a previously published comment they own | Pass |

---

#### Admin Tests

| Test | Result  |
|--|--|
| Admin can add chapters from adminpanel |Pass|
| Admin can add comments from adminpanel |Pass|
| Admin can update chapters from adminpanel |Pass|
| Admin can update comments from adminpanel |Pass|
| Admin can delete chapters from adminpanel |Pass|
| Admin can delete comments from adminpanel |Pass|
| Admin can create/update/delete user profiles from adminpanel |Pass|

---

### Validators

#### HTML
- [W3C HTML Validator](https://validator.w3.org/)
    - Checked all HTML-fiels checked.
    - Had minor errors mostly called by the django templating inside the HTML.
        - Errors corrected by [commit: b15573e](https://github.com/Rakdoslover/project-4-story/commit/b15573e31dafd501b9720b6330692526b2dfd3d4)
        - The remaining validation issues are all attributed to Django Templating not being recognized by W3C:
            - **Warning**: Consider adding a `lang` attribute to the `html` start tag to declare the language of this document
            - **Error**: Non-space characters found without seeing a doctype first. Expected `<!DOCTYPE html>`
            - **Warning**: This document appears to be written in English. Consider adding `lang="en"` (or variant) to the `html` start tag
            - **Error**: Element `head` is missing a required instance of child element `title`

#### CSS
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri)
    - No errors found.

#### Pip8 Validation
- [CI Python Linter](https://pep8ci.herokuapp.com/)
    - [settings.py](/media/pictures/settings.jpg)
    - [forms.py](/media/pictures/forms.jpg)
    - [models.py](/media/pictures/models.jpg)
    - [urls.py](/media/pictures/urls.jpg)
    - [views.py](/media/pictures/views.jpg)
        - No errors in code except settings.
        - The settings still shows 5 lines that're too long. These will not be correct due to them being installed/written by DJango. 

[Back to Top of page](#tcontents)

---

## Screenshots
<a name="screenshots"></a>

---

#### Home Page
---
Main page of my site, this is where we draw our users attention.
Here we can see the navbar with it's few but simple options(home, login & register),
the latest chapters sorted by newest to oldest and at the bottom a small footer.
![Home Page](/media/pictures/home-page.jpg)
##### Responsiveness Home Page
---
And here we have it opened and scaled down to 320px width.
The navbar is opened to show how it looks downscaled.
![Home Page 320px](/media/pictures/home-page-320.jpg)

#### Register Page
---
The register/signup page is based on the Allauth templates with some modifications.
It should be simple and easy to use, user should be able to just register a
username and a password to get access to the comment section.
![Register Page](/media/pictures/register-page.jpg)

##### Responsiveness Register Page
---
And here we have it opened and scaled down to 320px width.
![Register Page 320px](/media/pictures/register-page-320.jpg)

#### Login page
---
This is the login page for the users.
A simple page that takes the user back to the home page after signing in.
![Login Page](/media/pictures/login-page.jpg)

#####  Responsiveness Login Page
---
And here we have it opened and scaled down to 320px width.
![Login Page 320px](/media/pictures/login-page-320.jpg)

#### Logout Page
---
This is the logout page for the users.
A simple page that takes the user back to the home page after signing out.
![Logout Page](/media/pictures/logout-page.jpg)

#####  Responsiveness Logout Page
---
And here we have it opened and scaled down to 320px width.
![Logout Page 320px](/media/pictures/logout-page-320.jpg)

#### Chapter Page (upper)
---
This is where most of the interaction happens.
The chosen chapter, published by the author, is being displayed and the user can
see the placeholder image from the author and the story down below.
![Chapter Page upper](/media/pictures/chapter-text.jpg)

#### Chapter Page (lower)
---
Further down below the users can interact by uploading a proposed new title for
this weeks chapter, and also upload an image symbolizing the story.
This is where they can make use of the CRUD functionality for real.
While logged in you can Create, Read, Update and Delete your own comments.
![Chapter Page lower](/media/pictures/chapter-comment.jpg)

##### Responsiveness Chapter Page
---
And here we have it opened and scaled down to 320px width.
![Chapter Page 320px](/media/pictures/chapter-320.jpg)

#### Update Page
---
This is the Update page where the user can change their previous entries.
After a valid new form has been submitted, the button will take them back to the site.
This fulfills the U in CRUD.
![Update Page](/media/pictures/update-page.jpg)

##### Responsiveness Update Page
---
And here we have it opened and scaled down to 320px width.
![Update Page 320px](/media/pictures/update-page-320.jpg)

#### Delete Page
---
This is the Delete page where the user can delete their own comment.
After the button is pressed, it will take them back to the site.
This fulfills the D in CRUD.
![Delete Page](/media/pictures/delete-page.jpg)

##### Responsiveness Delete Page
---
And here we have it opened and scaled down to 320px width.
![Delete Page 320px](/media/pictures/delete-page-320.jpg)

[Back to Top of page](#tcontents)

---

## Future Implementations
<a name="future"></a>

---

<strong>1. Poll:</strong>
The initial idea was to create a poll for the user to voted on 1 of 2 choices
the story would take, at the end of the week the author would pick the choice
with the most votes and for the next chapter he/she would write it accordingly.

I started implementing this idea but never got past an issue were users could
vote multiple times and also vote for both. This is something I would like to
implement in the future because I like the idea of the user pushing the story
forward together with the author.

<strong>2. Reaction instead of likes:</strong>
I would be cool if the user would be able to express more than just a like.
Lets say the theme of the chapter was happiness/success, the user could express
a happy face. the same would be true about a chapter which had a theme of
sorrow they could express a sad face.

This idea only came to the idea stage, I thought about it but never really
looked in to how I would implement it. Maybe it would be in the same manor as
the likes system we did in the walkthrough for the blog but I'm not sure.

<strong>3. Comment on comment:</strong>
Another cool thing for my users would be if they could comment each others
comment, and give likes to other peoples suggested titles and images.
This would create a deeper "community" interactivity between users.

Just like the idea number 2, this one was only just an idea. It's a cool system,
sort of like comment system found on most sites like 9gag, reddit, etc..
I might look into the further on but at the moment it would be out of the scope
for this portfolio project.

<strong>4. User costumization:</strong>
I would like the users to have a chance to customize their own profiles, lets
say we're going to add a smaller shop och subscription profile to the site, it
would be a good idea for the users to have more control over their own pages.

This one doesn't seem far off as I think I will be able to apply this soon after
the E-commerce section is done.

### Problems/Errors left

#### Disclaimer:

There are 5 error indicating lines that're too long in my settings.py file,
I've intentionally left them in because they were created when django was
installed on the system. I've tried moving them but only gotten more errors.

<strong>Problem 1: Remains</strong>
Through my whole development process I've had this issue with a class "Chapter"
that still says it contains no objects. I've tried my best can't seem to solve
this issue.

<strong>Problem 2: Resolved</strong>
For a long time I didn't understand how to get the files from allauth copied for
my workspace. This coupled with the fact that I copied them manually made it
impossible to redirect the right static to the files.
It took both help from tutors and the slack community to address the issue but
it was resolved at last.

[Back to Top of page](#tcontents)

---

## Content
<a name="content"></a>
  
##### Django Documentation
  - Read through the django documentation multiple times to get to grips with the basics regarding models.

##### Geeks for Geeks.com
  - Used their walkthroughs and tips to get the CRUD just right for the comments CRUD by user.

##### Stackoverflow
  - I've read an ocean of questions and answers on Stackoverflow, some helpful some worthless.
    But when they actually helped me it really did the job.
  
##### W3 Schools
  - Used for reference throughout for simple HTML/CSS examples.
  
##### Code Institute
  - Course content for portfolio project 4 helped greatly in being able to complete this project.
  - Initial structure **based heavily** on the CI walkthrough of the "I Think Therefore I Blog".
  - Legacy code regarding Base/index.html and accompaning CSS remains.

[Back to Top of page](#tcontents)

---

## Credits
<a name="credits"></a>

##### Code institue Django3blog
- I started the project using the blog template from https://github.com/Code-Institute-Solutions/Django3blog
- This gave me a guide how to develop the project, install all parts and deploy to Heroku.
- It also gave me the starting baseline for my inital CSS/settings/url/models/Base and Index template/admin and start view functions.
- I copied and used the Allauth templates for sign-up/-in/-out 
- This allowed me to test with trial and error (with django documentations and stackoverflow as my handbook).

##### Mentoring
- I had a couple of down periods during this project and had a really hard time grasping exactly what I need, but my mentor allways pushed onwards.
- She had some really cool ideas, tip and tricks for me to test, that includes documentation to read or videos to watch.


##### [Dee Mc](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&ab_channel=DeeMc)
- A video series on Youtube describing really well how to get past some of the hurdles on my project.
- This was one of the tips I got from my mentor and it really did some wonders.

##### Tutor sessions
- Those hard hours were made so much easier by the giant help of the tutors.
- They've giving me alot of different ways to look at an issue and maybe getting it to work another way.

[Back to Top of page](#tcontents)


## Acknowledgements
<a name="acknowledgements"></a>

### My family
- I haven't been very chearful the last couple of weeks but my family has allways managed to put a smile on my face during the hardest hours.

[Back to Top of page](#tcontents)
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
<a name="contents">Back to Top</a>
 1. [ UX ](#ux)
 2. [Agile Development](#agile)
 3. [ Features ](#features)  
 4. [ Features Left to Implement ](#left)  
 5. [ Technology used ](#tech) 
 6. [ Testing ](#testing)  
 7. [ Bugs ](#bugs)  
 8. [ Credits](#credits)
 9. [ Content](#content)  
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

---

### User Stories

1. Create account

- As a User I can create an accout so that ** I can publish a comment**.

2.

-

## Testing

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
            - **Error**: 

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

### Screenshots
#### Home Page
---
Main page of my site, this is where we draw our users attention.
Here we can see the navbar with it's few but simple options(home, login & register),
the latest chapters sorted by newest to oldest and at the bottom a small footer.
[Home Page](/media/pictures/home-page.jpg)
##### Responsiveness Home Page
---
And here we have it opened and scaled down to 320px width.
The navbar is opened to show how it looks downscaled.
[Home Page 320px](/media/pictures/home-page-320.jpg)

#### Register Page
---
The register/signup page is based on the Allauth templates with some modifications.
It should be simple and easy to use, user should be able to just register a
username and a password to get access to the comment section.
[Register Page](/media/pictures/register-page.jpg)

##### Responsiveness Register Page
---
And here we have it opened and scaled down to 320px width.
[Register Page 320px](/media/pictures/register-page-320.jpg)

#### Login page
---
This is the login page for the users.
A simple page that takes the user back to the home page after signing in.
[Login Page](/media/pictures/login-page.jpg)

#####  Responsiveness Login Page
---
And here we have it opened and scaled down to 320px width.
[Login Page 320px](/media/pictures/login-page-320.jpg)

#### Logout Page
---
This is the logout page for the users.
A simple page that takes the user back to the home page after signing out.
[Logout Page](/media/pictures/logout-page.jpg)

#####  Responsiveness Logout Page
---
And here we have it opened and scaled down to 320px width.
[Logout Page 320px](/media/pictures/logout-page-320.jpg)

#### Chapter Page

## Future Implementations

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



## Content
  
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

[Back to Top of page](#content)

---

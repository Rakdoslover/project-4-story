# The Lonely Beach Project

## Description

This site hosts a story involving it's users.
Each week the author posts a story chapter without a title and placeholder
picture, the users may propose a title and a picture for this weeks chapter.
By the end of the week the author picks the one he/she likes the most and
renames the chapter and updates the picture accordingly.

##

## User Stories

1. Create account

- As a User I can create an accout so that ** I can publish a comment**.

2.

-

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

## Problems/Errors left

### Disclaimer:

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

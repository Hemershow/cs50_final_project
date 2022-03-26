# EBugo
#### Video Demo:  https://youtu.be/0w92mFKyX6o
#### Description:
My initial idea with this project was to try to create a website where conversations, explanations and warnings regarding game bugs would be accessible in a single place. Just like youtube did with videos on the internet. This way, when looking for a bug, it would be enough to type the name of the game in the same place as always, instead of searching random internet forums. The project is still far from being able to do that, to be that place. But with some time and several changes and additions I believe it is possible.

I had a lot of problems with the code and several things, especially the front-end went back to stage 0 multiple times. But it was fun and I got more comfortable with flask, sccs and programming in general.

I'm not sure what the name of this is, but from what I understand it’s a python flask-application. At the moment if you start the main file you will see a basic login / sign up page which upon login it will direct you to a home page. I must give credit to the video “Python Website Full Tutorial - Flask, Authentication, Databases & More
” (https://www.youtube.com/watch?v=dam0GPOAvVI&t=6458s) from Tech With Tim,  which helped me make sure this part is ok, when it comes to security and works.

All pages have a footer with the author, contact and a logo I made to try to give a face to the site or something. I have many ideas to implement, but for now as a skeleton of the project I want to complete, I'm satisfied! Especially with the looks, as it's nowhere near my strong point and there's been a lot of worse versions. That said, I will probably change a few things about that as well.
Ps: Just in case the text is somewhat poorly written, my mother's tongue is portuguese, I am still practising.

#### Project files:

##### website
Simply put, it is a folder that contains the website files, it helps to organize the project.

##### __pycache__
Is a folder automatically created by python when running a program, without going into many details, from what I understood after searching a little, it turns your code into bytecode, stores it and when run your program starts a little faster. If deleted, it will reappear after the program is started, unless this behavior is suppressed.

##### static
Folder where I stored the front end configurations of the site, where except for the images, all files are automatically created when adding scss to your code. Which I did to be able to edit settings of the bootstrap.
The main.scss file is where the css and bootstrap settings are defined, once edited and on its folder it is possible to run “sass main.scss main.css” and it will change the main.css file with all the bootstrap and css configurations. After that you just import the main.css file as a style sheet instead of a css file and bootstrap on your base html template.

##### templates
Folder where all the html pages are defined. The base file is being used as the main template for all of them, setting the navbar, footer, alert messages and importing the main.css style sheet. The following 6 html files just set what that specific page shows and does, importing things from the database, showing posts, forms, and in the case of the bug page, setting a javascript function, extending the base file. All of them are further explored on the “website pages” section.

##### __init__.py
File that sets the application, importing models, routes, authentication and initializing a secret key to encrypt cookies, also creates a database if it doesn’t already exist. 

##### auth.py
File in charge of computing the user authentication, containing all the logic behind the login or signing in. Register the user info, hashes passwords and compares them to the password input. Checks for already in use emails or usernames, remembers the current user.

##### database.db
Database file containing all the tables of information, currently they are Post, Comment and User. It stores them so that they can be easily accessed later on.

##### models.py
Python file that defines the tables of the database and their columns.

##### views.py
File that defines the routes of the website, containing each url and “GET”, “POST” logics. It chooses when to show, redirect or just show an alert message to the user, sends information to the html template pages and updates the database adding or removing elements.

##### main.py
File that makes the application run when executed

#### Website pages:

##### Home page
Upon entering, you will see a list of posts and a search bar. Currently, the only option for viewing posts is from the most recent to the oldest, something I intend to change soon. The search bar looks for post titles that contain what is searched. The posts contain the user who posted it, date, title, game and bug description. Every post is clickable and takes the user to a page for that specific bug.

##### Bug/id page
Here you will find the non-summarized version of a post that you have clicked, comments can be added, even if in a very simple way. If the user to access is the creator of the post, he can delete it along with its comments.

##### My bugs
This page is very similar to the home page, however it only shows the user's posts.

##### Post
Here the user will find a form where he enters the information for the creation of the post, at the moment the user himself types the game he is referring to and there is no filter regarding what he types. Both problems have solution ideas that are being studied as demonstrated in the video.

##### Logout
Clicking will automatically log out user and redirect to the login page


## License

MIT License

Copyright (c) 2021 Hemerson Da Silva Violin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


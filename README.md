
Credits:
Contributers to bloggawy and their finished tasks:
- Ahmed Helal:
   Review and edit the model and make it readable 
   make design bootstrap page for registration page	
   homepage posts retreiving 
   Complete and edit the design for the post page (comments and likes and post sections)
   Post page functionality (retreiving posts from data base, adding comments and replies, adding likes and dislikes, removing post after 10 dislikes and hashing forbidden words)
   All neccessary validation for the post page 
   
-Fadi El-Gawly:
   Home page functionality (home page design, retrieving and organizing posts from db, adding the subscribe/unsubscribe feature using ajax and base HTML )
   Login and logout functionality with the login form.

-Fahd Yousri:
  ERD for the models
  admin panel (adding new posts, tags, admin access validation and user blocking or promotion)
  reposatory managment (constructing and managing the repo, deviding tasks and following up with other team members  and integrating, reviewing and merging other members work)
  Post page initial design

-Fatma Kamel:
  Models and database construction.
  registration and login design
  registration functionality
  sending emails on registration and subscription

-Yasmin Abdallah
  admin panel (design and crud operations for users, posts, tags ,forbidden words and categories)
  Search with post title and tags   
  Pagination functionality to view 5 posts per page

Special thanks to:
Mohamed Ramadan and Ahmed Abdel-Fattah
for their support and continuous help in bringing this project to light.


Project description:
Welcome to the bloggawy project which is a django project for a blogging website applying the following requirements:
1- Landing Page Content​:
● Header:
Will contain Two links Login/Register. If the user is already logged in
then the link will be Logout. And If the logged in user is an admin,
then there will be another link called Manage Blog that will redirect
the admin to the administration page to make the admin CRUD
Operations.
● Sidebar:
Will contain all the available categories.
(example: Sports, News, Politics, ...) with a button beside them be
subscribe or unsubscribe if the user is already subscribed to this
category.
when a category is chosen it will be redirected to a page that
contains all the posts belongs to this category. Sorted by date of
publish
 ​when click on subscribe to a category confirmation email
would be send to the user with this message (Hello - user name -
you have subscribed successfully in - category name - welcome
aboard 
Will have top posts sorted by publish date.
when click on image of post. it will redirect to the post’s page.
● Footer:
Will have a pagination part where each page will contain only top 5
posts sorted by publish date.
When click on Next it will get me the next 5 posts.

2- Registration Page:
● It will be a form that takes:
○ Username
○ Email
○ Password
○ Password Confirmation (two must match )
○ (username and email are unique)

3-Login Page:
● Form contains 2 fields. Username & PW.
● Password will be shown in asterisks. when the user click on
login ,if he is blocked then redirect him back to login page with a
message (sorry you are blocked contact the admin)
● if he isn’t blocked then he will be authenticated.


4-Post Page Content:
● Title
● Post Picture
● Content of the post
● The category that this post is under
● Comments section
● Tags related
Post Page Characteristics:
● Each comment shows the time of the comment and the
username who wrote the comment.
● There will be a reply on comment just a single reply not a tree
reply like facebook.
● Add comment Section. User must be signed in to can submit a
comment (enter the text and a submit button to submit the comment)
● If the comment contains inappropriate words, It will show like **
With the length of the undesired word. For example:
[ ‘stupid’ → ****** ]
[ ‘fool’ → **** ]
● Like and dislike counter on the posts and if a post counted more
than 10 dislikes it will be auto deleted.
Normal user characteristics:
● He can see posts and categories
● Search by tagname, post title.
● If logged in he can like, dislike, comment and reply a comment on a
post.
● If blocked he cannot log into the system on login page
(Your account is locked, please contact an admin.)
Admin user characteristics:
● Admin users , can make CRUD on posts .
● Admin users , can make CRUD on categories
● Admin users, can block or unblock users .
● Admin users , can promote a normal user , that’s mean the prompted
user can login to /admins
● Admin users can CRUD on users .
● The Admin page will contains links
( users, posts, categories, forbidden words ).
● When Admin clicks on the Posts Link, It would list all posts, with links
to edit, delete and create.
same will be applied on categories, forbidden words
● When Admin clicks on Users Link, it would list all the users, in case
The user is also an admin, his row will be colored by red. Else it will
be a normal row.
● For the normal users there should be a button that enables the admin
to either lock or unlock this user from logging to the system. And for
the Admin users this button is not available So, an admin cannot lock
another admin.

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

### Connecting your Mongo database

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose **mongosh (2.0 or later)** for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- in the terminal, paste the copied code `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --apiVersion 1 --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password _(will not echo **\*\*\*\*** on screen)_

------

## Cultivating Intelligence
Go to [Repository](https://github.com/users/Josseyo/projects/4)
Go to live [website](https://github.com/users/Josseyo/projects/4)
Go to [README.md](https://github.com/Josseyo/Cultivating_Intelligence/main/README.md)


## Wireframes

## Features

## UX Design

**User flow**

1. View post list:
   - The user arrives at the homepage, which displays a list of all published posts.
   - The user can filter the posts by category using the filter option.
   - The user can click on a post to open the full text.

2. Open a post:
   - The user clicks on a post from the post list page.
   - The page displays the full text of the selected post.
   - The user can like, comment, or share the post using the provided buttons or links.

3. View likes:
   - On the post detail page, the user can see the number of likes displayed prominently.
   - The user can click on the likes count to see a list of users who have liked the post.

4. View comments:
   - On the post detail page, the user can see the comments displayed in a section below the post content.
   - The user can expand or collapse the comments section as needed.
   - If the user is an admin, they can view all comments on the site and filter or sort them.

5. Account registration:
   - If the user wants to comment or like a post, they need to register an account.
   - The user can click on the registration link or button from the main navigation.
   - The user is taken to the registration page, where they can enter their name, email, and password.
   - Upon successful registration, the user is logged in and redirected to the homepage.

The user can navigate between the different pages and features using the provided links, buttons, and navigation elements. The flow allows the user to view the post list, open a post, interact with the post (like, comment), and manage their account (registration).

## User Stories

- View post list: As a Site User I can view a list of posts so that I can select one to read
- View categories: As a Site User I can filter posts by category
- Open a post: As a Site User I can click on a post so that I can read the full text
- View likes: As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral
- View comments: As a Site User / Admin I can view comments on an individual post so that I can read the conversation
- Account registration: As a Site User I can register an account so that I can comment and like
- Comment on a post: As a Site User I can leave comments on a post so that I can be involved in the conversation
- Like / Unlike: As a Site User I can like or unlike a post so that I can interact with the content
- Manage posts: As a Site Admin I can create, read, update and delete posts so that I can manage my blog content
- Create drafts: As a Site Admin I can create draft posts so that I can finish writing the content later
- Approve comments: As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments

### User Account
### Site Admin
### Site Navigation
### Post Management
### Post comments
### Post Likes

## Wireframes

1. View post list:
   - The page displays a list of all published posts.
   - Each post shows the title, a brief excerpt, the author, and the date.
   - The user can click on a post to open the full text.
   - There are pagination controls to navigate through multiple pages of posts.
   - There is a filter option to allow the user to filter posts by category.

2. Open a post:
   - The page displays the full text of the selected post.
   - The post shows the title, author, date, and the full content.
   - There are buttons or links to allow the user to like, comment, or share the post.
   - The page also displays the number of likes and comments for the post.

3. View likes:
   - On the post detail page, the number of likes is displayed prominently.
   - There is a way for the user to see a list of users who have liked the post.
   - The admin can view the total number of likes for all posts on the site.

4. View comments:
   - On the post detail page, the comments are displayed in a section below the post content.
   - Each comment shows the commenter's name, the comment text, and the date/time of the comment.
   - There is a way for the user to expand or collapse the comments section.
   - The admin can view all comments on the site and filter or sort them.

5. Account registration:
   - The site has a dedicated registration page with fields for the user to enter their name, email, and password.
   - There is validation to ensure the email is valid and the password meets the site's requirements.
   - Upon successful registration, the user is logged in and redirected to the home page.
   - There is a link or button to access the registration page from the site's main navigation.

## Database Models
Link to ERD https://drive.google.com/file/d/1WCi45UnL2mnkBuHZyYrg0gmLmDXnZXu0/view?usp=sharing

#### User model
- Represents the users of the blog application. Each user has a unique username and email, a password, and timestamps for creation and update.

| Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- |
| username    |  ForeignKey   | User, on_delete=models.CASCADE  |
| created_on      | DateTimeField   | auto_now_add=True    |
| updated_on      | DateTimeField   | auto_now_add=True    |
| status      | IntegerField   |        |
| likes  |  ManyToManyField   |        |

#### Post model
- Represents the blog posts. Each post has a title, content, category, author (a reference to the User entity), and timestamps for publication, creation, and update.

![post_model](docs/images/models/post_model.png)

| Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- |
| title      | CharField | max_length=200, unique=True  |
| slug       | SlugField | max_length=100, unique=True  |
| author    |  ForeignKey   | User, on_delete=models.CASCADE  |
| category  | ForeignKey   | Category, on_delete=models.PROTECT, null=True  |
| excerpt   | TextField   |      |
| content     |TextField |      |
| image      | CloudinaryField  | 'image', default='placeholder'   |
| created_on      | DateTimeField   | auto_now_add=True    |
| updated_on      | DateTimeField   | auto_now_add=True    |
| status      | IntegerField   |        |
| likes  |  ManyToManyField   |        |

#### Comment model
- Represents the comments made on blog posts. Each comment has a reference to the post it belongs to (Post entity), the author of the comment (User entity), the comment content, and timestamps for creation and update.


#### Category model
 - Organize posts into different categories
 - Relationship: One-to-Many between Category and Post (a post can belong to one category, but a category can have multiple posts)

| Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- |
| name   | ForeignKey | Category, on_delete=models.CASCADE, related_name='category'   |
| description    |  TextField   | max_length=500 |
| created_on      | DateTimeField   | auto_now_add=True    |
| updated_on      | DateTimeField   | auto_now_add=True    |

#### Tag model
 Allow users to add tags to posts, making it easier to search and filter content.

| Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- |
| name   | String |   |
| created_on      | DateTimeField   | auto_now_add=True    |
| updated_on      | DateTimeField   | auto_now_add=True    |


#### Post Tag model
| Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- |
| description    |  TextField   | max_length=500 |
| created_on      | DateTimeField   | auto_now_add=True    |
| updated_on      | DateTimeField   | auto_now_add=True    |

#### Like model
 Allow users to express like to posts.

#### ERD Relationships:
- One-to-Many between User and Post: A user can have multiple posts, but each post is associated with only one user.
- One-to-Many between User and Comment: A user can have multiple comments, but each comment is associated with only one user.
- One-to-Many between Post and Comment: A post can have multiple comments, but each comment is associated with only one post.
- One-to-Many between Comment and Comment: A comment can have multiple replies, but each reply is associated with only one parent comment.
- One-to-Many between Category and Post: A post can belong to one category, but a category can have multiple posts
- Many-to-Many between Post and Tag: A tag can belong to multiple posts, and a post can have multiple tags.
- Many-to-Many between Post and User (a user can like multiple posts, and a post can have multiple likes from different users)


## Agile Methodology

Go to [Kanban board](https://github.com/users/Josseyo/projects/4)

A Kanban board with issues was created using GitHub Projects to manage the user stories and development process.

**MUSCOW**
The MVP contains the Must have functionality. 
The Should, Could and Would be nice to have is added to future development 

### Future development
#### Could have
- Nested Comments: Enable users to reply to specific comments, creating a hierarchical comment structure.

| Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- |
| post   | ForeignKey | Post, on_delete=models.CASCADE, related_name='comments'   |
| author    |  ForeignKey   | User, on_delete=models.CASCADE  |
| body     |TextField |   max_length=500   |
| created_on      | DateTimeField   | auto_now_add=True    |
| updated_on      | DateTimeField   | auto_now_add=True    |

# Cultivating Intelligence | Testing

## Code Validation

### HTML
### Code Validation

**HTML**
All HTML pages were validated using [W3C HTML Validator](https://validator.w3.org/) to check for any issues or syntax errors. Please see the results below for each page:

## Deployment


## Technologies

## Credits
-User stories, https://github.com/rockroman/CI_PP4-Knowledge-Flow/blob/main/README.md?plain=1
-User stories, https://github.com/ShizukaDonaghue/happy-beans/tree/main
-CI Django blog, https://www.youtube.com/watch?v=YH--VobIA8c&t=1453s
-Filter blog categories, https://www.youtube.com/watch?v=S9-Bt1JgRjQ
-Edit delete comments, CI LMS https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+3/courseware/713441aba05441dfb3a7cf04f3268b3f/21a16093c0084895a6073422447c3f7d/

-All icons are taken from Font Awesome (http://fontawesome.io/) project.
The Font Awesome font is licensed under the SIL OFL 1.1:
- https://scripts.sil.org/OFL

SVG icons source: https://github.com/encharm/Font-Awesome-SVG-PNG
Font-Awesome-SVG-PNG is licensed under the MIT license (see file license
in current folder).
## Process...

**Challenges** 
I edited and rearranged the user stories in Kanban board in the beginning of coding the project. I struggled a bit with writing them so they would match the code to be able to finish clear bites of user stories to be able to move functionl bits to done in Kanban.

Issues with CI database caused interuptions, confusion and unclear commits when trying to solve issue outside my reach. 
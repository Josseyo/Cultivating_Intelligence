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


## Database Schema

## Agile Methodology

Go to [Kanban board](https://github.com/users/Josseyo/projects/4)

A Kanban board with issues was created using GitHub Projects to manage the user stories and development process.

# Cultivating Intelligence | Testing

## Code Validation

### HTML
### Code Validation

**HTML**
All HTML pages were validated using [W3C HTML Validator](https://validator.w3.org/) to check for any issues or syntax errors. Please see the results below for each page:

## Deployment


## Technologies

## Credits
User stories, https://github.com/rockroman/CI_PP4-Knowledge-Flow/blob/main/README.md?plain=1
User stories, 

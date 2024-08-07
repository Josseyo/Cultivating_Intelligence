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


---

# Cultivating Intelligence

[View Live Website](https://cultivating-intelligence-1ead7384db49.herokuapp.com/)  
[View Repository](https://github.com/users/Josseyo/projects/4)  
[View README.md](https://github.com/Josseyo/Cultivating_Intelligence/main/README.md)

## Table of Contents

- [Wireframes](#wireframes)
- [Features](#features)
- [UX Design](#ux-design)
- [User Stories](#user-stories)
- [Design](#design)
- [Database](#database)
- [Code Structure](#code-structure)
- [Agile Methodology](#agile-methodology)
- [Testing](#testing)
- [Deployment](#deployment)
- [Bugs](#bugs)
- [Issues/Improvements](#issuesimprovements)
- [Technologies](#technologies)
- [Credits](#credits)
- [Process](#process)

## Wireframes

*(Add wireframe images or links here)*

## Features

- User registration and login
- Post creation, editing, and deletion
- Like and comment functionality
- Category filtering for posts
- Admin panel for managing content

## UX Design

### User Flow

1. **View Post List**: Users arrive at the homepage displaying all published posts, with options to filter by category.
2. **Open a Post**: Users can click on a post to view its full content, along with options to like, comment, or share.
3. **View Likes**: Users see the number of likes on the post and can view a list of users who liked it.
4. **View Comments**: Users can view and interact with comments below each post, including admin functionalities for comment management.
5. **Account Registration**: Users must register to like or comment, with a straightforward registration process.

### User Stories

- As a Site User, I can view a list of posts to select one to read.
- As a Site User, I can click on a post to read its full text.
- As a Site User, I can navigate to different category pages to read sorted posts.
- As a Site User, I can view the number of likes to identify popular posts.
- As a logged-in Site User, I can view comments on a post to engage in discussions.
- As a logged-in Site User, I can leave comments on posts to add my input
- As a logged-in Site User, I can like or unlike posts, to show my appreciation 
- As a Site Admin, I can manage posts and comments effectively.

## Design

### Colors

*(Specify color palette)*

### Fonts

*(Specify font choices)*

## Database

### Entity-Relationship Diagram (ERD)

<details><summary>Click to view ERD</summary>
<img src="docs/...">
</details>

- The database structure is based on a PostgreSQL model, representing tables, columns, relationships, and constraints.

### Database Models

- **User Model**: Represents users with unique usernames and emails.
- **Post Model**: Contains details for each blog post, including title, content, and author.
- **Comment Model**: Manages comments associated with posts.
- **Category Model**: Organizes posts into categories.
- **Like Model**: Allows users to express likes for posts.

### ERD Relationships

- One-to-Many: User to Post
- One-to-Many: User to Comment
- One-to-Many: Post to Comment
- Many-to-Many: Post to User (likes)

## Code Structure

The project code is organized within application folders, constructed using the Django framework.

### Project Apps

*(List project apps here)*

### Other Django Apps

- **settings.py**: Configuration settings for the Django project.
- **Procfile**: Commands for deploying the Django app.
- **static**: Base CSS and JavaScript files.
- **templates**: Base-level and app-specific HTML templates.
- **requirements.txt**: Lists dependencies for the project.
- **env.py**: Stores environment variables securely.

## Agile Methodology

[View Kanban Board](https://github.com/users/Josseyo/projects/4)

A Kanban board was created using GitHub Projects to manage user stories and the development process.

### MUSCOW Prioritization

- **Must Have**: Core functionalities for MVP.
- **Should Have**: Important features for future development.
- **Could Have**: Enhancements for user experience.
- **Would Be Nice To Have**: Additional features for future consideration.

### Future Development

- **Could Have**: Nested comments for hierarchical discussions.
- **Tags**: Allow users to tag posts for easier searching.

## Testing

### Code Validation

- **HTML**: Validated using [W3C HTML Validator](https://validator.w3.org/).

## Deployment

*(Include deployment instructions)*

## Bugs

[View Bug Documentation](https://docs.google.com/document/d/1ebW5cHddPkr2NpX6HFFQn2LsT-bAh9Y6OB7q3mzyrgo/edit)

## Issues/Improvements

- Consistency in typography, including text and heading levels.

## Technologies

*(List technologies used)*
- CI Database: https://dbs.ci-dbs.net/

## Credits

- User Stories Reference: [GitHub Repository 1](https://github.com/rockroman/CI_PP4-Knowledge-Flow/blob/main/README.md?plain=1)
- CI Django Blog Tutorial: [YouTube Video](https://www.youtube.com/watch?v=YH--VobIA8c&t=1453s)
- Font Awesome: [Font Awesome](http://fontawesome.io/)

### Imagery

- Post images from: [Stock Cake](https://stockcake.com)
- Default blog post image from [Unsplash](https://unsplash.com...)

## Process

### Challenges

- Rearranging user stories in the Kanban board was challenging initially.
- Issues with the CI database caused interruptions and confusion.
- Maintaining documentation in GitHub was time-consuming.

---


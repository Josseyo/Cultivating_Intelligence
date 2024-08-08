
---

# Cultivating Intelligence

[View Live Website](https://cultivating-intelligence-1ead7384db49.herokuapp.com/)  
[View Repository](https://github.com/Josseyo/Cultivating_Intelligence)  

[View README.md](https://github.com/Josseyo/Cultivating_Intelligence/main/README.md)

[View Kanban and agile project](https://github.com/users/Josseyo/projects/4)

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

1. **View Post List**: Users arrive at the homepage displaying all published posts, with options to filter by category from the menu in the navbar.
2. **Open a Post**: Users can click on a post to view its full content, along with options to like, comment, or share.
3. **View Likes**: Users can see the number of likes on the post.
4. **View Comments**: Users can view and interact with comments below each post, including edit and delete user's own comments.
5. **Account Registration**: Users must register to like or comment, with a straightforward registration process.
6. **Blog management**: Admin can log in to django dashboard to view, sort, add, edit and delete; posts, comments, likes, categories, and users.

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

| Element               | Color                     | Hex Code   |
|-----------------------|---------------------------|------------|
| Background                 | Light Gray                      | #XXXXXX   |
| Title                 | Blue                      | #233D4D   |
| Headlines             | Orange                    | #FE7F2D   |
| Excerpt               | Turquoise                 | #619B8A   |
| Body Text             | Dark Gray                 | #333333   |
| Likes                 | Yellow                    | #FCCA46   |
| Categories            | Green                     | #A1C181   |
| Comments              | Turquoise                 | #619B8A   |
| Edit Button           | Orange                    | #FE7F2D   |
| Delete Button         | Red                       | #FF4D4D   |
| Create Account Button  | Green                     | #A1C181   |
| Login Button          | Blue                      | #233D4D   |
| Logout Button         | Red                       | #FF4D4D   |


These colors have been chosen based on their psychological effects, aiming to enhance user experience and support individuals with Attention Deficit Hyperactivity Disorder (ADHD).

### 1. Blue (#233D4D)
- **Calming Effect and Focus Enhancement**: Blue promotes tranquility, helping to reduce anxiety and improve concentration while reading or engaging with content.
- **Usage:** Use for the main title to create a calming and focused impression.

### 2. Orange (#FE7F2D)
- **Energy and Enthusiasm**: Orange stimulates mental activity and can make the blog feel more inviting and engaging. 
- **Usage**: Use for section headlines to grab attention and energize the content.
- **(Orange (#FE7F2D) for edit, Red (e.g., #FF4D4D) for delete.
Usage: Use orange for edit buttons to signify action, and a contrasting red for delete buttons to indicate caution.)**

### 3. Yellow (#FCCA46)
- **Optimism and Attention-Grabbing**: Yellow is uplifting and can enhance mood, making the reading experience more enjoyable. This bright hue effectively highlights important information or calls to action, without overwhelming the user.

### 4. Green (#A1C181)
- **Balance and Harmony**: Green evokes a sense of calmness and balance, creating a soothing environment for readers. This color can help reduce visual fatigue, making it easier for users to engage with longer articles.
- **Usage:** Use for category labels to convey balance and organization.

### 5. Turquoise (#619B8A)
- **Refreshing and Invigorating for Mental Clarity**: Turquoise combines the calming effects of blue with the uplifting qualities of green, providing a refreshing visual experience. This color enhances clarity and encourages communication.
- **Usage:** Use this refreshing color for excerpts to encourage readers to engage with the content.

The selected color palette is designed to create an engaging and supportive environment for users, particularly those with ADHD, ensuring a cohesive and user-friendly interface that enhances readability and interaction throughout the blog.

- **Blue** #233D4D
- **Orange** #FE7F2D
- **Yellow** #FCCA46
- **Green** #A1C181
- **Turkose** #619B8A

[Colors](docs/images/colors.png)

<details><summary>Click to view colors</summary>
<img src="docs/images/colors.png">
</details>

### Fonts

*(Specify font choices)*

## Database
I have used [CI Database](https://dbs.ci-dbs.net/) for the project.

### Entity-Relationship Diagram (ERD)

  User {
    int id PK
    string username
    string email
  }
  
  Category {
    int id PK
    string name
  }
  
  Post {
    int id PK
    string title
    string slug
    int status
    string excerpt
    string content
    datetime created_on
    datetime updated_on
    int likes_count
  }
  
  Comment {
    int id PK
    string body
    datetime created_on
    boolean approved
  }
  
  User ||--o{ Post : "writes" }
  User ||--o{ Comment : "writes"}
  Category ||--o{ Post : "categorizes" }
  Post ||--o{ Comment : "receives" }
  User ||--o{ Post : "likes" }


<details><summary>Click to view ERD</summary>
<img src="docs/images/models/blog_erd.png">

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
***
- The flow was tested during and post development
    - Device Testing
    - Browser Compatibility
    - Manual Testing

### Code Validation

- **HTML**: Validated using [W3C HTML Validator](https://validator.w3.org/).
### CSS
- [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)was used  to validate the css in the project
    - web app passed validator with no errors. 
    <details><summary>Style.css</summary>
    <img src="docs/validation/html-css/valid-css.png" width="800">
    </details>

### Html
- [WC3 Validator](https://validator.w3.org/) was used to validate the html in the project

- Note : all info on validator pages are related with using cloudinary template tags for rendering user uploaded images and there for trailing slash cant be removed
    

<details><summary>Home</summary>
<img src="docs/validation/html-css/home-html-valid.png" width="800" >
</details>

<details><summary>Register</summary>
<img src="docs/validation/html-css/signup-valid.png" width="800" >
</details>

<details><summary>Login</summary>
<img src="docs/validation/html-css/login-valid.png" width="800" >
</details>


<details><summary>Blog</summary>
<img src="docs/validation/html-css/blog.png" width="800" >
</details>

<details><summary>Blog detail</summary>
<img src="docs/validation/html-css/blog-detail-valid.png" width="800" >
</details>

<details><summary>Category</summary>
<img src="docs/validation/html-css/category-valid.png" width="800" >
</details>

<details><summary>Comment ad/edit/delete</summary>
<img src="docs/validation/html-css/blog-edit.png" width="800">
</details>


   
### Javascript
- [JShint](https://jshint.com/) was used to validate custom script file

    <details><summary>Js file</summary>
    <img src="docs/validation/python-js/custom-js.png" width="800" >
    </details>

### Python
- [CI Python Linter](https://pep8ci.herokuapp.com/) to check  Python code for validity and conventions

    <details><summary>Home app</summary>

    <details><summary>views.py</summary>
    <img src="docs/validation/python-js/home-views.png" width="800" >
    </details>

    <details><summary>urls.py</summary>
    <img src="docs/validation/python-js/home-url.png" width="800" >
    </details>

    <details><summary>forms.py</summary>
    <img src="docs/validation/python-js/home-forms.png" width="800" >
    </details>
 
    </details>

    ***

    <details><summary>cultivating_intelligence_blog app</summary>

    <details><summary>views.py</summary>
    <img src="docs/validation/python-js/blog-views2.png" width="800" >
    </details>

    <details><summary>urls.py</summary>
    <img src="docs/validation/python-js/blog-urls.png" width="800" >
    </details>

    <details><summary>forms.py</summary>
    <img src="docs/validation/python-js/blog-forms.png" width="800" >
    </details>

    <details><summary>models.py</summary>
    <img src="docs/validation/python-js/blog-models.png" width="800" >
    </details> 
    </details>

    ***

    <details><summary>categories app</summary>

    <details><summary>views.py</summary>
    <img src="docs/validation/python-js/categories-views.png" width="800" >
    </details>

    <details><summary>urls.py</summary>
    <img src="docs/validation/python-js/category-url.png" width="800" >
    </details>

    <details><summary>models.py</summary>
    <img src="docs/validation/python-js/categories-models.png" width="800" >
    </details>
    </details>

    ***   

### Lighthouse

- [Lighthouse](https://developers.google.com/web/tools/lighthouse/) used for analyzing performance, accessibility and SEO for the project. Below are the results of the analysis:
 
<details><summary>Home Desktop-screen</summary>
<img src="docs/validation/lighthouse/home-desk.png" >

</details>
<details><summary>Home Mobile-screen</summary>
<img src="docs/validation/lighthouse/Home-mob.png" >
</details>

<details><summary>Register page Desktop-screen</summary>
<img src="docs/validation/lighthouse/register-desk.png">
</details>
<details><summary>Register page Mobile-screen</summary>
<img src="docs/validation/lighthouse/register-mob.png">
</details>

<details><summary>Login Desktop-screen</summary>
<img src="docs/validation/lighthouse/login-desk.png" >
</details>

<details><summary>Login page Mobile-screen</summary>
<img src="docs/validation/lighthouse/login-mob.png">
</details>

<details><summary>Blog detail Desktop-screen</summary>
<img src="docs/validation/lighthouse/blog-detail-desk.png">
</details>

<details><summary>Blog detail Mobile-screen</summary>
<img src="docs/validation/lighthouse/blog-detail-mob.png">
</details>

<details><summary>Comment edit Desktop-screen</summary>
<img src="docs/validation/lighthouse/comment-edit-desk.png">
</details>

<details><summary>Comment edit Mobile-screen</summary>
<img src="docs/validation/lighthouse/comment-edit-mob.png">
</details>

<details><summary>Category Desktop-screen</summary>
<img src="docs/validation/lighthouse/category-desk.png">
</details>

<details><summary>Category Mobile-screen</summary>
<img src="docs/validation/lighthouse/category-mob.png">
</details>

### Wave
 [Wave Validator](https://wave.webaim.org/) to evaluate accessibility

<details><summary>Home</summary>
<img src="docs/validation/wave/home-pg.png" width="800" height="1200" >
</details>

<details><summary>Register</summary>
<img src="docs/validation/wave/register-pg.png" width="800" height="1200">
</details>

<details><summary>Login</summary>
<img src="docs/validation/wave/login-pg.png" width="800" height="1200">
</details>

<details><summary>Logout</summary>
<img src="docs/validation/wave/logout-pg.png" width="800" height="1200">
</details>

<details><summary>Confirm logout</summary>
<img src="docs/validation/wave/logout-pg.png" width="800" height="1200">
</details>

<details><summary>Blog detail</summary>
<img src="docs/validation/wave/blog-detail.png" width="800" >
</details>

<details><summary>Category</summary>
<img src="docs/validation/wave/category-pg.png" width="800" >
</details>

## Testing
***

- The project was tested during and post development and all
results for 
    - Device Testing
    - Browser Compatibility
    - Manual Testing

## Bugs

[View Bug Documentation](https://docs.google.com/document/d/1ebW5cHddPkr2NpX6HFFQn2LsT-bAh9Y6OB7q3mzyrgo/edit)

## Heroku Deployment

Before deploying to Heroku, ensure you have the following variables prepared:

- **Database URL**
- **SECRET_KEY** (You can generate one [here](https://miniwebtool.com/django-secret-key-generator/))
- **CLOUDINARY_URL** (After logging in to the Cloudinary website, copy the 'Cloudinary URL' from your account dashboard)

### Step-by-step Instructions

1. **Create `env.py`**: At the root level of your project, create a file named `env.py` and add the following lines, replacing the placeholders with your actual values:

   ```python
   import os

   os.environ['DATABASE_URL'] = 'your_Database_URL'
   os.environ['SECRET_KEY'] = 'your_secret_key'
   os.environ['CLOUDINARY_URL'] = 'your_cloudinary_url'
   ```

2. **Sign Up or Log In to Heroku**:
   - Go to the [Heroku website](https://www.heroku.com/) and sign up or sign in to your account.

3. **Create a New App**:
   - From the Heroku dashboard, click on "Create New App."
   - Choose a unique name for your app and select the appropriate region, then click on the 'Create App' button.

4. **Set Up Environment Variables**:
   - Navigate to the 'Settings' tab of your newly created app.
   - Click on 'Reveal Config Vars' and add the following environment variables:
     - `DATABASE_URL`: Your Database URL
     - `SECRET_KEY`: Your generated secret key
     - `CLOUDINARY_URL`: Your Cloudinary URL
     - `DISABLE_COLLECTSTATIC`: Set this variable to `1` (this can be removed after the initial deployment)
     - `PORT`: Set this variable to `8000`

5. **Deploy Your App**:
   - Select the 'Deploy' tab from the dashboard.
   - In the Deployment method section, choose "Connect to GitHub."
   - Find your GitHub repository by name and connect it.
   - At the bottom of the page, select either "Automatic Deploys" or "Manual Deploys" based on your preference.

6. **Start the Deployment Process**:
   - Click on the option you chose, and you should see the deployment process begin.

---

## Forking the GitHub Repository

1. **Log In or Sign Up**:
   - Go to [GitHub](https://github.com/) and log in or create an account.

2. **Access the Repository**:
   - Navigate to the [GitHub repository](https://github.com/Josseyo/Cultivating_Intelligence).

3. **Fork the Repository**:
   - Click the "Fork" button in the top right corner.
   - A copy of the repository will be created in your own GitHub account.

---

## Cloning a GitHub Repository

1. **Go to the Repository**:
   - Visit the [GitHub repository](https://github.com/Josseyo/Cultivating_Intelligence).

2. **Locate the Code Button**:
   - Click the "Code" button above the list of files (next to 'Add file').

3. **Choose a Cloning Option**:
   - Select either HTTPS or GitHub CLI as your preferred cloning method.

4. **Open Git Bash**:
   - Launch Git Bash on your computer.

5. **Change Directory**:
   - Navigate to the directory where you want to clone the repository.

6. **Clone the Repository**:
   - Type the following command, replacing the URL with the one you copied:

   ```bash
   git clone https://github.com/Josseyo/Cultivating_Intelligence
   ```

7. **Press Enter**:
   - Hit Enter to create your local clone of the repository.

---


## Issues/Improvements

- Consistency in typography, including text and heading levels.

## Technologies

- CI Database: https://dbs.ci-dbs.net/

## Credits

- User Stories Reference: [CI Blog user stories](https://github.com/Code-Institute-Solutions/BlogUserStories/blob/main/userstories.md)
- User Stories Reference: [GitHub Repository Rockroman](https://github.com/rockroman/CI_PP4-Knowledge-Flow/blob/main/README.md?plain=1)
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


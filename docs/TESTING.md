# Manual Testing

### Registration
- [X] **Navigate to Sign-Up page**: `/account/signup/`
- [X] **Fill registration form with valid details**: 
  - Username, email, password
- [X] **Submit registration form**
- [X] **Verify registration success**:
  - User is redirected to Home page (index page)

### Logout
- [X] **Navigate to Sign-Out page**: `/account/logout/`
- [X] **Sign-Out**
- [X] **Verify Sign-Out success**:
  - User is redirected to the Home page (index page)

### Login
- [X] **Navigate to Sign-In page**: `/account/login/`
- [X] **Enter valid credentials and log in**
- [X] **Verify login success**:
  - User is redirected to the Home page (index page)

### Add a Comment
- [X] **Navigate to a specific post's detail page**: `/posts/<slug>/`
- [X] **Add a comment to the post**
- [X] **Submit comment form**
- [X] **Verify comment creation success**:
  - Comment is displayed under the post

### Delete a Comment
- [X] **Delete a comment**
- [X] **Verify comment deletion success**:
- User is redirected to the post detail page where the comment is deleted.

### Edit a Comment
- [X] **Edit a comment**
 - takes you to the edit comment page:`/posts/<slug>/edit_comment/`
- [X] **The comment form is prefilled with the comment to edit**
- [X] **Verify comment update success**:
 -User is redirected to the post detail page

### Like a Post
- [X] **Like a post**
- [X] **Unlike a post**

### 404 page
-[X] **Redirected to 404 page**
-[X] **Go back to Home**

### General Functionality
- [X] **Verify home page displays latest posts**:
  - Ensure pagination is working (6 posts per page)

### Responsiveness
- [X] **Check responsiveness**:
  - Ensure the website looks good and works well on phones, tablets, and computers

### Contact Page
- [X] **Navigate to Contact page**: `/contact/`
- [X] **Enter valid contact information and submit request**
- Ensure a valid email address is entered
- [X] **Verify contact request submit**:

### Error Handling
- [X] **Test invalid login attempt**:
  - Enter incorrect credentials and submit
  - Verify appropriate error message is displayed

- [X] **Test invalid form submissions**:
  - Leave required fields empty and submit forms
  - Verify appropriate error messages are displayed

### Security
- [X] **Ensure password is not visible when typing**


### Deployment
- [X] **Check deployment settings**:
  - Ensure `DEBUG` is set to `False` in production
- [X] **Verify static file serving**:
  - Ensure static files (CSS, JS, images) are loading correctly in production

### Miscellaneous
- [X] **Verify all links and buttons work as expected**
- [X] **Ensure no broken images on the site**


### Responsiveness
- [X] **The website is fully responsive across all screen sizes**
- [X] **Images maintain their quality without any pixelation or distortion**
- [X] **Page elements are arranged to prevent overlapping**
- [X] **Horizontal scrolling is completely avoided**


### Code Validation

- **HTML** Validated using [W3C HTML Validator](https://validator.w3.org/)
- **CSS** Validated using [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
- **Javascript** validated using [JS hint](https://jshint.com)
- **Python** validated using [CI Python Linter](https://pep8ci.herokuapp.com/)
- **Performance** validated using [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
- **Accessibility** validated using [Wave Validator](https://wave.webaim.org/) 



### Html
[W3C HTML Validator](https://validator.w3.org/) was used to validate html templates

#### HTML validated without errors

<details><summary>Home</summary>
<img src="images/validation/home-html-valid.png" width="800" >
</details>

<details><summary>Register (errors)</summary>
Unsolved errors in Django signup template:
<img src="images/validation/signup-html-error.png" width="800" >
</details>


<details><summary>Login</summary>
<img src="images/validation/login-html-valid.png" width="800" >
</details>

<details><summary>Logout</summary>
<img src="images/validation/logout-html-valid.png" width="800" >
</details>

<details><summary>Blog detail (error)</summary>
Unsolved error in Django admin add post: 
<img src="images/validation/blog-detail-html-error.png" width="800" >

![blog detail error](images/validation/blog-detail-html-error2.png)
</details>

<details><summary>Category</summary>
<img src="images/validation/category-html-valid.png" width="800">
</details>

<details><summary>Comment edit</summary>
<img src="images/validation/comment_edit_html.png" width="800">
</details>
***
<details><summary>Some Html errors and fixes</summary>
<img src="images/validation/html_errors.png" width="800">
</details>

### CSS validated without errors
[Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/) was used to validate the css styling

<details><summary>Home</summary>
<img src="images/validation/css-home-valid.png" width="800" >
</details>

<details><summary>Blog post</summary>
<img src="images/validation/css-blog-detail-valid.png" width="800">
</details>

   
### Javascript
[JShint](https://jshint.com/) was used to validate the custom Javscript files

<details><summary>Comments.js</summary>
<img src="images/validation/comments-js-valid.png" width="800">
</details>


<details><summary>Cookies.js</summary>
<img src="images/validation/js-cookies-valid.png" width="800" >
</details>


### Python
[CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code.


   **<details><summary>Blog app - Python files </summary>**
   <img src="images/validation/blog_python_validation.png" width="800" >
   </details>

   **<details><summary>Contact app - Python files </summary>**
   <img src="images/validation/contact_python_validation.png" width="800" >
   </details>

   **<details><summary>Cultivating Intelligence - Python files </summary>**
   <img src="images/validation/cultivating_intelligence_python_validation.png" width="800" >
   </details>


---


### Lighthouse

[Lighthouse](https://developers.google.com/web/tools/lighthouse/) used for analyzing performance, accessibility and SEO for the project. Below are the results of the analysis:
 
<details><summary>Home Desktop-screen</summary>
<img src="images/validation/lighthouse-home-desk.png" width="800" >
</details>

<details><summary>Home Mobile-screen</summary>
<img src="images/validation/lighthouse-home-mob.png" width="800" >
</details>


<details><summary>Contact page Desktop-screen</summary>
<img src="images/validation/lighthouse-contact-desk.png" width="800">
</details>


<details><summary>Contact page Mobile-screen</summary>
<img src="images/validation/lighthouse-contact-mob.png" width="800">
</details>


<details><summary>Blog detail Desktop-screen</summary>

<img src="images/validation/lighthouse-blog-detail-desktop-screen.png" width="800"> 

To improve Accessibility I added alt text to the icons:
<img src="images/validation/add_alt_attribute.png" width="800"> 
</details>

<details><summary>Blog detail Mobile-screen</summary>
<img src="images/validation/lighthouse-blog-detail-mob.png" width="800">
</details>

<details><summary>Category Desktop-screen</summary>
<img src="images/validation/lighthouse-category-desk.png" width="800" >

</details>

<details><summary>Category Mobile-screen</summary>
<img src="images/validation/lighthouse-category-mob.png" width="800">

[Category Mobile-screen](https://pagespeed.web.dev/analysis/https-cultivating-intelligence-1ead7384db49-herokuapp-com-category-Workplace%20Strategies/ehokhlzwbe?form_factor=mobile&category=performance&category=accessibility&category=best-practices&category=seo&hl=sv&utm_source=lh-chrome-ext)
</details>

<details><summary>Comment edit Desktop-screen</summary>
<img src="images/validation/lighthouse-comment-edit-desk.png" width="800">

[Comment edit Desktop-screen](https://pagespeed.web.dev/analysis/https-cultivating-intelligence-1ead7384db49-herokuapp-com-adhd-always-deeply-highly-dedicated-edit_comment-127/o50n6hpg0o?use_original_url=true&hl=sv&form_factor=desktophttps://pagespeed.web.dev/analysis/https-cultivating-intelligence-1ead7384db49-herokuapp-com-adhd-always-deeply-highly-dedicated-edit_comment-127/o50n6hpg0o?use_original_url=true&hl=sv&form_factor=desktop)
</details>

<details><summary>Comment edit Mobile-screen</summary>
<img src="images/validation/lighthouse-comment-edit-mob.png" width="800">

[Comment edit Mobile-screen](https://pagespeed.web.dev/analysis/https-cultivating-intelligence-1ead7384db49-herokuapp-com-adhd-always-deeply-highly-dedicated-edit_comment-127/o50n6hpg0o?use_original_url=true&hl=sv&form_factor=mobile)
</details>

<details><summary>Register page Desktop-screen</summary>
<img src="images/validation/lighthouse-register-desk.png" width="800">


[Register page Desktop-screen](https://pagespeed.web.dev/analysis/https-cultivating-intelligence-1ead7384db49-herokuapp-com-accounts-signup/p39w03m9g3?form_factor=desktop&category=performance&category=accessibility&category=best-practices&category=seo&hl=sv&utm_source=lh-chrome-ext)

</details>

<details><summary>Register page Mobile-screen</summary>
<img src="images/validation/lighthouse-register-mob.png" width="800">

[Register page Mobile-screen](https://pagespeed.web.dev/analysis/https-cultivating-intelligence-1ead7384db49-herokuapp-com-accounts-signup/p39w03m9g3?form_factor=mobile&category=performance&category=accessibility&category=best-practices&category=seo&hl=sv&utm_source=lh-chrome-ext)

</details>

---

### Wave
[Wave Validator](https://wave.webaim.org/) to evaluate accessibility

<details><summary>Home</summary>
<img src="images/validation/home-pg.png" width="800" height="1200" >
</details>

<details><summary>Register</summary>
<img src="images/validation/register-pg.png" width="800" height="1200">
</details>

<details><summary>Login</summary>
<img src="docs/validation/login-pg.png" width="800" height="1200">
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
<img src="images/validation/category.png" width="800" >
</details>

---

### Errors and fixes

<details><summary>Some errors and fixes along the way</summary>
<img src="images/validation/errors_fixes.png" width="800" >
</details>
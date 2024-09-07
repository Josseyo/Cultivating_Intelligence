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
  - Takes you to the edit comment page: `/posts/<slug>/edit_comment/`
- [X] **The comment form is prefilled with the comment to edit**
- [X] **Verify comment update success**:
  - User is redirected to the post detail page

### Like a Post
- [X] **Like a post**
- [X] **Unlike a post**

### 404 Page
- [X] **Redirected to 404 page**
- [X] **Go back to Home**

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
[W3C HTML Validator](https://validator.w3.org/) was used to validate HTML templates.

#### HTML Validated Without Errors

<details><summary>Home</summary>
<img src="images/validation/home-html-valid.png" width="800">
</details>

<details><summary>Register (errors)</summary>
Unsolved errors in Django signup template:
<img src="images/validation/signup-html-error.png" width="800">
</details>

<details><summary>Login</summary>
<img src="images/validation/login-html-valid.png" width="800">
</details>

<details><summary>Logout</summary>
<img src="images/validation/logout-html-valid.png" width="800">
</details>

<details><summary>Blog Detail (error)</summary>
Unsolved error in Django admin add post: 
<img src="images/validation/blog-detail-html-error.png" width="800">
![Blog Detail Error](images/validation/blog-detail-html-error2.png)
</details>

<details><summary>Category</summary>
<img src="images/validation/category-html-valid.png" width="800">
</details>

<details><summary>Comment Edit</summary>
<img src="images/validation/comment_edit_html.png" width="800">
</details>

---

<details><summary>HTML Errors and Fixes</summary>
<img src="images/validation/html_errors.png" width="800">
</details>

### CSS Validated Without Errors
[Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS styling.

<details><summary>Home</summary>
<img src="images/validation/css-home-valid.png" width="800">
</details>

<details><summary>Blog Post</summary>
<img src="images/validation/css-blog-detail-valid.png" width="800">
</details>

### Javascript
[JShint](https://jshint.com/) was used to validate the custom Javascript files.

<details><summary>Comments.js</summary>
<img src="images/validation/comments-js-valid.png" width="800">
</details>

<details><summary>Cookies.js</summary>
<img src="images/validation/js-cookies-valid.png" width="800">
</details>

### Python
[CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code.

**<details><summary>Blog App - Python Files</summary>**
<img src="images/validation/blog_python_validation.png" width="800">
</details>

**<details><summary>Contact App - Python Files</summary>**
<img src="images/validation/contact_python_validation.png" width="800">
</details>

**<details><summary>Cultivating Intelligence - Python Files</summary>**
<img src="images/validation/cultivating_intelligence_python_validation.png" width="800">
</details>

---

### Lighthouse

[Lighthouse](https://developers.google.com/web/tools/lighthouse/) used for analyzing performance, accessibility, and SEO for the project. 

For latest improvements, follow the link in the beginning of each section:

<details><summary>Home Desktop Screen</summary>

[Home Desktop Screen](https://pagespeed.web.dev/analysis/https-cultivating-intelligence-1ead7384db49-herokuapp-com/5wce22rjex?form_factor=desktop&category=performance&category=accessibility&category=best-practices&category=seo&hl=sv&utm_source=lh-chrome-ext) 
<img src="images/validation/lighthouse-home-desk.png" width="800">
</details>

<details><summary>Home Mobile Screen</summary>

[Home Mobile Screen](https://pagespeed.web.dev/analysis/https-cultivating-intelligence-1ead7384db49-herokuapp-com/5wce22rjex?form_factor=mobile&category=performance&category=accessibility&category=best-practices&category=seo&hl=sv&utm_source=lh-chrome-ext)
<img src="images/validation/lighthouse-home-mob.png" width="800">
</details>

<details><summary>Contact Page Desktop Screen</summary>

[Contact Desktop Screen](https://pagespeed.web.dev/analysis/https-cultivating-intelligence-1ead7384db49-herokuapp-com-contact-contact/vaxw748m9x?form_factor=desktop&category=performance&category=accessibility&category=best-practices&category=seo&hl=sv&utm_source=lh-chrome-ext)
<img src="images/validation/lighthouse-contact-desk.png" width="800">
</details>

<details><summary>Contact Page Mobile Screen</summary>

[Contact Mobile Screen](https://pagespeed.web.dev/analysis/https-cultivating-intelligence-1ead7384db49-herokuapp-com-contact-contact/vaxw748m9x?form_factor=mobile&category=performance&category=accessibility&category=best-practices&category=seo&hl=sv&utm_source=lh-chrome-ext)
<img src="images/validation/lighthouse-contact-mob.png" width="800">
</details>

<details><summary>Blog Detail Desktop Screen</summary>

[Blog Detail Desktop Screen](https://pagespeed.web.dev/analysis/https-cultivating-intelligence-1ead7384db49-herokuapp-com-sensory-friendly-spaces/oaxyoxkz03?form_factor=desktop&category=performance&category=accessibility&category=best-practices&category=seo&hl=sv&utm_source=lh-chrome-ext)
<img src="images/validation/add_alt_attribute.png" width="800"> 
</details>

<details><summary>Blog Detail Mobile Screen</summary>

[Blog Detail Mobile Screen](https://pagespeed.web.dev/analysis/https-cultivating-intelligence-1ead7384db49-herokuapp-com-sensory-friendly-spaces/oaxyoxkz03?form_factor=mobile&category=performance&category=accessibility&category=best-practices&category=seo&hl=sv&utm_source=lh-chrome-ext)
<img src="images/validation/lighthouse-blog-detail-mob.png" width="800">
</details>

<details><summary>Category Desktop Screen</summary>

[Category Desktop Screen](https://pagespeed.web.dev/analysis/https-cultivating-intelligence-1ead7384db49-herokuapp-com-category-Workplace%20Strategies/ehokhlzwbe?form_factor=desktop&category=performance&category=accessibility&category=best-practices&category=seo&hl=sv&utm_source=lh-chrome-ext)
<img src="images/validation/lighthouse-category-desk.png" width="800">
</details>

<details><summary>Category Mobile Screen</summary>

[Category Mobile Screen](https://pagespeed.web.dev/analysis/https-cultivating-intelligence-1ead7384db49-herokuapp-com-category-Workplace%20Strategies/ehokhlzwbe?form_factor=mobile&category=performance&category=accessibility&category=best-practices&category=seo&hl=sv&utm_source=lh-chrome-ext)
<img src="images/validation/lighthouse-category-mob.png" width="800">
</details>

<details><summary>Comment Edit Desktop Screen</summary>

[Comment Edit Desktop Screen](https://pagespeed.web.dev/analysis/https-cultivating-intelligence-1ead7384db49-herokuapp-com-adhd-always-deeply-highly-dedicated-edit_comment-127/o50n6hpg0o?use_original_url=true&hl=sv&form_factor=desktop)
<img src="images/validation/lighthouse-comment-edit-desk.png" width="800">
</details>

<details><summary>Comment Edit Mobile Screen</summary>

[Comment Edit Mobile Screen](https://pagespeed.web.dev/analysis/https-cultivating-intelligence-1ead7384db49-herokuapp-com-adhd-always-deeply-highly-dedicated-edit_comment-127/o50n6hpg0o?use_original_url=true&hl=sv&form_factor=mobile)
<img src="images/validation/lighthouse-comment-edit-mob.png" width="800">
</details>

<details><summary>Register Page Desktop Screen</summary>

[Register Page Desktop Screen](https://pagespeed.web.dev/analysis/https-cultivating-intelligence-1ead7384db49-herokuapp-com-accounts-signup/p39w03m9g3?form_factor=desktop&category=performance&category=accessibility&category=best-practices&category=seo&hl=sv&utm_source=lh-chrome-ext)
<img src="images/validation/lighthouse-register-desk.png" width="800">
</details>

<details><summary>Register Page Mobile Screen</summary>

[Register Page Mobile Screen](https://pagespeed.web.dev/analysis/https-cultivating-intelligence-1ead7384db49-herokuapp-com-accounts-signup/p39w03m9g3?form_factor=mobile&category=performance&category=accessibility&category=best-practices&category=seo&hl=sv&utm_source=lh-chrome-ext)
<img src="images/validation/lighthouse-register-mob.png" width="800">
</details>

---

### Wave
[Wave Validator](https://wave.webaim.org/) to evaluate accessibility.

<details><summary>Home</summary>
<img src="images/validation/home-pg.png" width="800" height="1200">
</details>

<details><summary>Register</summary>
<img src="images/validation/register-pg.png" width="800" height="1200">
</details>

<details><summary>Login</summary>
<img src="images/validation/login-pg.png" width="800" height="1200">
</details>

<details><summary>Logout</summary>
<img src="images/validation/wave/logout-pg.png" width="800" height="1200">
</details>

<details><summary>Confirm Logout</summary>
<img src="images/validation/wave/logout-pg.png" width="800" height="1200">
</details>

<details><summary>Blog Detail</summary>
<img src="images/validation/wave/blog-detail.png" width="800">
</details>

<details><summary>Category</summary>
<img src="images/validation/category.png" width="800">
</details>

---

### Errors and Fixes

<details><summary>Some Errors and Fixes Along the Way</summary>
<img src="images/validation/errors_fixes.png" width="800">
</details>

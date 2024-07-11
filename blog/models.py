from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Status for Post model
STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)


# Media type choices for Post model
MEDIA_TYPE = (
    (0, 'Text'),
    (1, 'Video'),
    (2, 'Pod')
)


# Category type choices for Post model
CATEGORY_TYPE = (
    (0, 'ADHD in the Workplace'),
    (1, 'Workplace Strategies'),
    (2, 'Stress and Emotional Regulation'),
    (3, 'Education and Inclusive Practices'),
    (4, 'Career Development and Advancement'),
    (5, 'Communication and Interpersonal Skills'),
)

# Models
""" 
User Model,
as part of the Django allauth library contains basic information about authenticated user and contains folowing fields:
username, password,email
"""

""" 
Post Model,
to create and manage blog posts:
    Title - post title
    Slug - to store and generate valid URL path automatically
    Author - post author, assigned by username automatically
    Category_type - category type such as category 1 & category 2, used for post filter
    Media_type - media type such as text, video & pod, used for post filter
    Excerpt - post description  
    Body - post content
    Image - post image, if none provided, a default image is displayed
    Created_on - post creation date, used to organise recipes in order
    Updated_on - post update date, used for admin purposes
    Status - post status, draft or published
    Likes - number of likes by users
"""
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    
    excerpt = models.TextField(blank=True)
    category = models.IntegerField(
        verbose_name="Category", choices=CATEGORY_TYPE)
    media = models.IntegerField(
        verbose_name="Media", choices=MEDIA_TYPE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        """
        Ordering of posts by their creation dates in descending order
        """
        ordering = ['-created_on']

    def _str_(self):
        """Returns post title as a string"""
        return self.title()

    def number_of_likes(self):
        """Returns total number of likes for each post"""
        return self.likes.count() 

""" 
Comment Model,
to create and manage comments:
    Name - comment author, assigned by username automatically
    Email - user email, assigned by user email automatically
    Content - comment content
    Created_on - comment creation date, used to organise comments in order
    Updated_on - comment update date, used for admin purposes
"""
class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80) 
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    Updated_on = models.DateTimeField(auto_now=True)
   
    class Meta:
        """
        Order comments by their creation dates in ascending order
        """    
        ordering = ['created_on']
    
    def _str_(self):
        """Returns comment body and author name"""    
        return f"Comment {self.body} by {self.name}"

    def date_format_created_on(self):
        """Date formatting for creation dates"""
        return self.created_on.strftime('%d %b %Y')
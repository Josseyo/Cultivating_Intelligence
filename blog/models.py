from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

# Status for Post model
STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
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
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blogpost_like', blank=True)

    class Meta:
        """
        Ordering of posts by their creation dates in descending order
        """
        ordering = ['-created_on']

    def __str__(self):
        """Returns post title as a string"""
        return self.title

    def number_of_likes(self):
        """Returns total number of likes for each post"""
        return self.likes.count() 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

""" 
Comment Model,
to create and manage comments:
    Auther - comment author, assigned by username automatically
    Email - user email, assigned by user email automatically
    Content - comment content
    Created_on - comment creation date, used to organise comments in order
    Updated_on - comment update date, used for admin purposes
"""
class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    #name = models.CharField(max_length=80) 
    #email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Order comments by their creation dates in ascending order
        """    
        ordering = ['created_on']

    def __str__(self):
        """Returns comment body and author"""    
        return f"Comment {self.body} by {self.author}"



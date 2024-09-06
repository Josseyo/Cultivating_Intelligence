from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

"""
Status for Post model
"""
STATUS = ((0, "Draft"), (1, "Publish"))


class Category(models.Model):
    """
    Model for blog category.

    Attributes:
        name (str): The name of the category.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Returns the name of the category as a string.
        """
        return self.name


class Post(models.Model):
    """
     Post model to create and managing blog post:

    Attributes:
         title (str): Title of the post.
         category (Category): The category the post belongs to.
         slug (str): A URL-friendly version of the title.
         author (User): Author of the post.
         featured_image (CloudinaryField): Image representing the post.
         excerpt (str): Short summary of the post.
         content (str): Main content of the post.
         created_on (datetime): Date and time the post was created.
         updated_on (datetime): Date and time the post was last updated.
         status (int): Publication status of the post (Draft or Publish).
         likes (ManyToManyField): Users who liked the post.
    """

    title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField("image", default="placeholder")
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name="blogpost_like", blank=True
    )

    class Meta:
        """
        Meta class for Post model for ordering the posts

        Attributes:
            ordering (list): Specifies the default ordering of posts
            by creation date in descending order.
        """

        ordering = ["-created_on"]

    def __str__(self):
        """Returns the title of the post as a string."""
        return self.title

    def number_of_likes(self):
        """Returns the total number of likes for each post."""
        return self.likes.count()

    def save(self, *args, **kwargs):
        """Overrides default save method to auto-generate slug from title."""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Comment model for creating and managing comments on blog posts.

     Attributes:
         post (Post): The post to which the comment belongs.
         author (User): Author of the comment.
         body (str): Content of the comment.
         created_on (datetime): Date and time the comment was created.
         updated_on (datetime): Date and time the comment was last updated.
         approved (bool): Indicates if comment is approved for publication,
         default is set to True.
    """

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=True)

    class Meta:
        """
        Meta options for Comment model.

        Attributes:
            ordering (list): Default ordering of comments by creation
            date in ascending order.
        """

        ordering = ["created_on"]

    def __str__(self):
        """Returns string of the comment including body and author."""
        return f"Comment {self.body} by {self.author}"

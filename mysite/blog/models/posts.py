from django.db import models
from django.contrib.auth.models import User

STATUS = [
    (0, "Draft"),
    (1, "Publish"),
]

class Post(models.Model):
    """Relational Model for Posts

    Args:
        title(char): Title of the post;
        slug(Slug): Field for text e special;
        author(User): The user that owns the post;
        updated_on(Date): Date when the post was last updated;
        created_on(Date): Date when the post was created;
        status(choices[STATUS]): If the post is published;
        content(Text): Content of the post;
    """
    
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    content = models.TextField()
    
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title
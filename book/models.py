from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


# Main storyline chapter model
class Chapter(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="book_chapter"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Review(models.Model):

    post = models.ForeignKey(Chapter, on_delete=models.CASCADE,
                             related_name="reviews")
    name = models.CharField(max_length=80)
    proposed_title = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f'Review {self.proposed_title} by {self.name}'

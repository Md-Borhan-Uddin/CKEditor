from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    CATEGORY = (
        ('Sport','Sport'),
        ('Fashon','Fashon')
    )
    title = models.CharField(max_length=200)
    discription = RichTextField()
    category = models.CharField(max_length=50, choices=CATEGORY)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
from turtle import title
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from .functions import get_random_alphanumeric_string


# Create your models here.

class Category(models.Model):
    CATEGORY = (
    ('Frontend' , 'Frontend'),
    ('Backend' , 'Backend'),
    ('Fullstack' , 'Fullstack')
    )
    category = models.CharField(max_length=50, choices=CATEGORY, default='Frontend')

    def __str__(self):
        return f'{self.category}'


class Post(models.Model): 
    STATUS = (
    ('Published' , 'Published'),
    ('Draft' , 'Draft')
    )
    title = models.CharField(max_length=40)
    content = models.TextField()
    post_pic = models.ImageField(upload_to='post_pics', blank=True,  null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS, default='Published')
    slug = models.SlugField(null=False, blank=True, editable=False)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=17)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) + '-' + get_random_alphanumeric_string(8)
        super().save(*args, **kwargs)


class Comment(models.Model):
    content = models.TextField(max_length=300)
    date_stamp = models.DateTimeField(auto_now_add=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)

class Like(models.Model):
    who_liked = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)

class PostView(models.Model):
    who_viewed = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)


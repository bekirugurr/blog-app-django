from turtle import title
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


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
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    post_pic = models.ImageField(upload_to='post_pics', blank=True)
    publish_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS, default='Published')
    slug = models.SlugField(null=False, blank=True, editable=False)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=17)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)




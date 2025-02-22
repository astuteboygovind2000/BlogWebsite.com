from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

# Create your models here.
# we use this model to change details of admin
class Home(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    about = models.TextField()
    copyright = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    linkdin = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.first_name


class Catagory(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    text = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()


    def __str__(self):
        return self.name
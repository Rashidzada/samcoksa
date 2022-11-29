from django.db import models
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length=400)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    img = models.ImageField(upload_to='img',blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=230)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = RichTextField()
    replay = RichTextField(blank=True)

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=200)
    profile = models.CharField(max_length=200,help_text="Give a name etc Sale man or manager, or Suppler")
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    description = RichTextField()
    img = models.ImageField(upload_to='img',verbose_name="Background Image", max_length=200, help_text="MAX 400kb")
    img1 = models.ImageField(upload_to='img',blank=True,verbose_name="Profile Image",max_length=100,help_text="MAX 200kb")
    qualification = models.CharField(max_length=200, default="MCS")
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=200,unique = True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    description = models.TextField(blank=True)
    description_detail = RichTextField(blank=True)
    author_img = models.ImageField(blank=True,upload_to="img")
    img = models.ImageField(blank=True,upload_to="img")

    video = EmbedVideoField(blank=True)

    def __str__(self):
        return str(self.title)+ " By " +str(self.author)


class ContactU(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=26)
    email = models.EmailField()
    whatApp = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    tw = models.URLField(blank=True)
    linkedin= models.URLField(blank=True)

    def __str__(self):
        return str(self.name)+" and "+ str(self.location)


class Team(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    img = models.ImageField(upload_to='img',blank=True)

    def __str__(self):
        return self.name
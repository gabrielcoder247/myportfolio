from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    github_acct = models.CharField(max_length=30)
    proj_image = models.ImageField(upload_to='portfolio/')
    pub_date = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    about = models.TextField(max_length=30)
    skills = models.CharField(max_length=30)
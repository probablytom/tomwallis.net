from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.TextField()
    content = models.TextField()

class Project(models.Model):
    title = models.TextField()
    summary = models.TextField()
    url = models.TextField()
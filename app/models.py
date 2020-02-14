from django.db import models

class Genre(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateTimeField('publish date')
    
class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateTimeField('publish date')
    genre = models.ManyToManyField(Genre)


from django.db import models
from django.forms import ModelForm

class Genre(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateTimeField('publish date', auto_now_add=True, blank=True)
    def __str__(self):
        return self.title

class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateTimeField('publish date', auto_now_add=True, blank=True)
    genre = models.ManyToManyField(Genre)
    def __str__(self):
        return self.title

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description']
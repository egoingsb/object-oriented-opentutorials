from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Topic, TopicForm, Genre, GenreForm

# Create your views here.
def index(request, topic_id=None):
    item = None
    if(topic_id):
        item=Topic.objects.get(id=topic_id)
    return render(request, 'app/topic_read.html', {
        'contents':Topic.objects.all(),
        'content':item,
        'mode':'topic'
    })
    

def topic_create(request):
    if(request.method == "POST"):
        form = TopicForm(request.POST)
        if(form.is_valid()):
            post = form.save()
            return redirect('/')
    return render(request, 'app/topic_create.html', {
        'form':TopicForm(),
        'contents':Topic.objects.all(),
        'mode':'topic'
    })


def genre_read(request, genre_id=None):
    item = None
    if(genre_id):
        item=Genre.objects.get(id=genre_id)
    return render(request, 'app/genre_read.html', {
        'contents':Genre.objects.all(),
        'content':item,
        'mode':'genre'
    })


def genre_create(request):
    if(request.method == "POST"):
        form = GenreForm(request.POST)
        if(form.is_valid()):
            post = form.save()
            return redirect('/genre')
    return render(request, 'app/genre_create.html', {
        'form':GenreForm(),
        'contents':Genre.objects.all(),
        'mode':'genre'
    })


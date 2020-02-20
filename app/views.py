from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Topic, TopicForm, Genre, GenreForm
from bs4 import BeautifulSoup
from django.contrib import messages


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
    form = TopicForm()
    if(request.method == "POST"):
        form = TopicForm(request.POST)
        if(form.is_valid()):
            genre_tag = [y for x in form.cleaned_data['genre'] for y in BeautifulSoup(x.description, 'html.parser').findAll(['h1','h2','h3','h4','h5','h6'])]
            description_tag = BeautifulSoup(form.cleaned_data['description'], 'html.parser').findAll(['h1','h2','h3','h4','h5','h6'])
            diff = set(genre_tag) - set(description_tag)
            if len(diff):
                messages.error(request, '장르와 일치하지 않습니다.요소가 누락 되었습니다'.join([str(tag) for tag in diff]))
            else:
                post = form.save()
                return redirect('/')

    return render(request, 'app/topic_create.html', {
        'form':form,
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


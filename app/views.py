from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Topic, TopicForm, Genre, GenreForm
from bs4 import BeautifulSoup
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'app/index.html', {})

def search_index(request, keyword=""):
    genres = Genre.objects.all()
    return render(request, 'app/search.html', {
        'contents':genres,
        'keyword':keyword
    })


def topic_index(request):  
    return render(request, 'app/topic_index.html', {
        'contents':Topic.objects.all(),
        'mode':'topic'
    })

def topic_read(request, topic_id=None):
    item = None
    if(topic_id):
        item=Topic.objects.get(id=topic_id)    
        genres = item.genre.all()
        return render(request, 'app/topic_read.html', {
            'contents':Topic.objects.all(),
            'content':item,
            'genres':genres,
            'mode':'topic'
        })

# def topic_read(request, topic_id=None):
#     item = None
#     if(topic_id):
#         item=Topic.objects.get(id=topic_id)
#     return render(request, 'app/t_read.html', {
#         'contents':Genre.objects.all(),
#         'content':item,
#         'topics':topics,
#         'mode':'genre'
#     })

    
def topic_create(request):
    form = TopicForm()
    if(request.method == "POST"):
        form = TopicForm(request.POST)
        if(form.is_valid()):
            genre_tag = [y for x in form.cleaned_data['genre'] for y in BeautifulSoup(x.description, 'html.parser').findAll(['h1','h2','h3','h4','h5','h6'])]
            description_tag = BeautifulSoup(form.cleaned_data['description'], 'html.parser').findAll(['h1','h2','h3','h4','h5','h6'])
            diff = set(genre_tag) - set(description_tag)
            if len(diff):
                messages.error(request, '장르와 일치하지 않습니다.요소가 누락 되었습니다\n'+','.join([str(tag) for tag in diff]))
            else:
                post = form.save()
                return redirect('/topic/'+str(post.id))

    return render(request, 'app/topic_create.html', {
        'form':form,
        'contents':Topic.objects.all(),
        'mode':'topic'
    })


def genre_read(request, genre_id=None):
    item = None
    topics = []
    if(genre_id):
        item=Genre.objects.get(id=genre_id)
        topics = Topic.objects.filter(genre__id=genre_id)
    return render(request, 'app/genre_read.html', {
        'contents':Genre.objects.all(),
        'content':item,
        'topics':topics,
        'mode':'genre'
    })


def genre_read_one(request, genre_id):
    item=Genre.objects.get(id=genre_id)
    return JsonResponse({'title':item.title, 'desc':item.description})


def genre_create(request):
    if(request.method == "POST"):
        form = GenreForm(request.POST)
        if(form.is_valid()):
            post = form.save()
            return redirect('/genre/'+str(post.id))
    return render(request, 'app/genre_create.html', {
        'form':GenreForm(),
        'contents':Genre.objects.all(),
        'mode':'genre'
    })


from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Topic, TopicForm

# Create your views here.
def index(request, topic_id=None):
    topic = None
    if(topic_id):
        topic=Topic.objects.get(id=topic_id)
    return render(request, 'app/topic_read.html', {
        'contents':Topic.objects.all(),
        'content':topic
    })

def topic_create(request):
    if(request.method == "POST"):
        form = TopicForm(request.POST)
        if(form.is_valid()):
            post = form.save()
            return redirect('/')
    return render(request, 'app/topic_create.html', {'form':TopicForm()})


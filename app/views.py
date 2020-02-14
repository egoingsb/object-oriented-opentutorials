from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic

# Create your views here.
def index(request, topic_id=None):
    topic = None
    if(topic_id):
        topic=Topic.objects.get(id=topic_id)
    return render(request, 'app/topic_read.html', {
        'contents':Topic.objects.all(),
        'content':topic
    })


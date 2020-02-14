from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic

# Create your views here.
def index(request):
    return render(request, 'app/index.html', {
        'contents':Topic.objects.all()
    })


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topic/create', views.topic_create),
    path('topic/<int:topic_id>', views.index),
    path('genre/', views.genre_read),
    path('genre/create', views.genre_create),
    path('genre/<int:genre_id>', views.genre_read),
    path('genre_json/<int:genre_id>', views.genre_read_one)
]

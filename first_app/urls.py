from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.help,name='help'),
    path('help',views.help,name='help'),
    path('access',views.access,name='access'),
    path('webpage',views.webpage,name='webpage'),
    path('topic',views.topic,name='topic'),
]

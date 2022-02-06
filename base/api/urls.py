import imp
from os import rename
from unicodedata import name
from django.urls import path

from base import api
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('note-list/', views.noteList, name='note-list'),
    path('note-detail/<str:pk>/', views.noteDetail, name='note-detail'),
    path('note-create/', views.noteCreate, name='note-create'),
    path('note-update/<str:pk>/', views.noteUpdate, name='note-update'),
    path('note-last/', views.noteLast, name='note-last'),

    path('leaf-tag/', views.leafTag, name='leaf-tag'),

]
    # path('note-delete/<str:pk>/', views.noteDelete, name='note-delete'),


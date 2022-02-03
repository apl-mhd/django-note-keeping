from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('save/', views.save_note, name='save'),
    path('save-category',views.save_category, name='save-category'),
]
from django.contrib import admin
from django.urls import path
from snippetsapp import views

urlpatterns = [
    path('new/', views.snippet_new, name='snippet_new'),
    path("<int:snippet_id>/edit/", views.snippet_edit, name='snippet_edit'),
    path("<int:snippet_id>/", views.snippet_detail, name='snippet_detail'),
]

from . import views

from django.urls import path

urlpatterns = [
    path('',views.MovieListView.as_view(), name='index'),
    
]

from django.shortcuts import render

from .serializers import MovieSerializer
from .models import MovieData

from django.views.generic import ListView

from rest_framework import viewsets

# Views in DRF :
# Learn the views, viewssets and other imp. concepts used in DRF 
# in the ChatGPT based pdf I downloaded - Django DRF concepts viewsets.pdf
# Also available at  https://chatgpt.com/share/67487807-c61c-8002-a992-9811a3cde1d0

# Views in DRF are similar to Django's regular views but are adapted for APIs.
# They also can be function based or class based.

# DRF also has generic views, which provide common patterns of CRUD
# operations for repetetive tasks. ListAPIView, CreateAPIView, etc

# DRF also provide mixins which combine Reusable components into custom views

# Viewsets in DRF :
# They combine logic of multiple views( List, Retreive, CRUD etc)
# into a single class.
# They work closely with routers to simplify URL routing (DRF has its own routing)
# Again learn more about them - Django DRF concepts viewsets.pdf

# We will use ModelViewSet, Most commonly used viewset for APIs.
# It is a specialized type of viewset for models.
# and Provides all CRUD operations ( list , retrieve , create , update , delete ) by default.

class MovieViewSet(viewsets.ModelViewSet):
    # As in the case of class-based views (CBVs) in Django, we can set 
    # attributes to define the default behavior of the base class. 
    # If we want to change this behavior, we can override its methods.
    
    queryset = MovieData.objects.all()  # This specifies the queryset that the viewset will operate on.
                        # Here, it retrieves all records from the MovieData model.
                        # If filtering is required, this can be overridden using `get_queryset()`.
    
    serializer_class = MovieSerializer # This says that, For all CRUD API
                        # operations on Movie model, appy the serializer
                        # We defined earlier.
# Now set up main urls.py in project root.
# But study these first : https://www.django-rest-framework.org/api-guide/routers/
# https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/

# Now We need to add API endpoints, Why? Note that Above viewset gives all
# data at once, What if enduser wants to filter, based on fields like genre
# Hence to send specific part of data only we need to assign urls, that
# give filtered results to endusers.

class DramaMovieViewSet( viewsets.ModelViewSet):
    queryset = MovieData.objects.filter( genre = 'Drama') # Just give drama
    serializer_class = MovieSerializer # Note that I also added, genre to
                                       # fields of the serializer
    
# But I cant keep doing the same thing over again, also If we do, 
# What happens when there is new genre? Hence lets have a general
# viewset that takes genre as param from API request and handles accordingly

# First note that When user sends request for genre he will send as
# /genre/Action or /genre/Drama etc, Hence
# our router registration for this viewset must take the genre part and 
# save it as path parameter. 

# router.register(r'genre/(?P<genre>[\w-]+)', GenreMovieViewSet, basename='genre_movies')
    # learn this RegExp here : https://chatgpt.com/share/6748ca44-4f88-8002-97de-63c9fec8f7cc
    # also in the chatgpt pdf downloaded : GenreMovieViewSet.pdf

class GenreMovieViewSet( viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    # Now since we want to customize queryset that will be filter,
    # We will extend the get_queryset() method hence property not necessary

    def get_queryset(self):
        # We need to get path params passed by user, but since we use
        # named grouping with p<genre> it will saved as key-val pair 
        # In all CBVs, kwargs is a dictionary attached to each class (self.kwargs)
        # that stores the variables captured from the URL pattern (the "dynamic" parts of the URL)
        genre_url = self.kwargs.get('genre') # get the genre from url

        # Now filter and return the queryset
        return MovieData.objects.filter(genre=genre_url)
    # Now go back and register this viewset to router
#----------------------Template Views from Now on----------------

class MovieListView(ListView ):
    model = MovieData
    context_object_name = 'movies'
    template_name = 'index.html'


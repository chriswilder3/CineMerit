from django.shortcuts import render

from .serializers import MovieSerializer
from .models import MovieData

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







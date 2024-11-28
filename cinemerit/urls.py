"""
URL configuration for cinemerit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from movies.views import MovieViewSet, DramaMovieViewSet
from rest_framework import routers
# read more : https://www.django-rest-framework.org/api-guide/routers/
# https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/
# Routers provide an easy and structured way to define the URLs for your API
# endpoints and automatically handle the routing of HTTP requests to the
# appropriate viewsets just like urlpatterns. Read chatgpt pdf : https://chatgpt.com/share/6748b26c-c400-8002-b6d9-416147ca5ab4

# The Default router is same as Simplerouter, But it adds an additional
# feature
router = routers.DefaultRouter() 

router.register('movies',MovieViewSet, basename='all_movies')
                         # We can access movies using /movies/ 
                         # Now this router acts like an app's internal router 
                         # before, if we add it to urlpattern using 'include' 

# Since we are adding another model, this causes error if we register multiple
#  ViewSets for the same model especially since modelname is used as default
# basename if unspecified. So Its always good to give basenames.
router.register('drama',DramaMovieViewSet, basename ='drama_movies')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]


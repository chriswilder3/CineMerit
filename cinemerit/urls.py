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

from .views import MovieViewSet
from rest_framework import routers
# read more : https://www.django-rest-framework.org/api-guide/routers/
# https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/
# Routers provide an easy and structured way to define the URLs for your API
# endpoints and automatically handle the routing of HTTP requests to the
# appropriate viewsets just like urlpatterns. Read chatgpt pdf : https://chatgpt.com/share/6748b26c-c400-8002-b6d9-416147ca5ab4

router = routers.DefaultRouter() # While SimpleRouter maps viewsets to URLs
                        # without appending any prefix, DefaultRouter adds prefit
                        # ie, /(root) we can use to lists all viewsets under it.

router.register('movies',MovieViewSet)  # We need to access using /movies/data 
                         # Now this router acts like app's internal router
                         # before, if we add it to urlpattern using 'include' 


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]


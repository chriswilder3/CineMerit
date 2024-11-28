from django.db import models

# Create your models here.

class MovieData( models.Model):
    name = models.CharField( max_length= 255)
    duration = models.FloatField( ) # In minutes
    rating = models.FloatField( )

    # This was added after creation of viewset,router etc
    genre = models.CharField( max_length = 100, null = True)
    

    def __str__(self):
        return f' {self.name} '



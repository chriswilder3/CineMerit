from rest_framework import serializers

from .models import MovieData

# Serializer are imp part of API building, they are used to convert 
# complex datatype like Django model instances into python datatypes
# so that further down the line they can be converted into 
# common API data formats like JSON , XML

# Read more here : https://www.geeksforgeeks.org/serializers-django-rest-framework/
# Read the 1st example and comment serializer, 


# Serializers are defined very similar to models/forms
class MovieSerializer( serializers.ModelSerializer):
    # Now you know how serializer works, What its output is, 
    # Model serializer is a part of DRF that is used to create a serializer
    # containing the fields corresponding to fields in a model.

    # It will automatically generate a set of fields for you, based on the model.
    # It will automatically generate validators for the serializer, such as unique_together validators.
    # It includes simple default implementations of .create() and .update()
    # Hence We define model and fields inside its Meta class just 
    # like in the form to create it.

    class Meta:
        model = MovieData
        fields = ['id', 'name', 'duration', 'rating']
        # Remember id is part of model by default.
        # Its better to include id as part of JSON for better API access.

# As seen in GFG example, these serializers are initialized and appied on
# various objects (like python objects or model instances) in Python code.
# Since Our aim is to output these to the requested clients, We can make
# use of django views to apply all the logic of API building.

# Remember : Serializers After applying on objects or model instances
# We apply .data() method, whichs gives data that is very similar
# to Python Dictory (which can be converted to JSON easily)
# Ex : {'id': 1, 'name': 'Inception', 'duration': 148.0, 'rating': 8.8}
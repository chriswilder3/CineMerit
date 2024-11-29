# Movie API with Django Rest Framework

This project is a Movie API built with Django Rest Framework (DRF). The API allows users to retrieve information about various movies, filter movies based on genre, and perform CRUD operations. This project is created as part of a resume project to showcase skills in building RESTful APIs using Django Rest Framework.

## Features

- List all movies
- Retrieve a specific movie
- Create a new movie
- Update an existing movie
- Delete a movie
- Filter movies by genre

## Models

### MovieData
The `MovieData` model contains the following fields:
- `id`: IntegerField (primary key)
- `name`: CharField
- `duration`: FloatField
- `rating`: FloatField
- `genre`: CharField
- `image`: ImageField

## Serializers

### MovieSerializer
The `MovieSerializer` is a `ModelSerializer` for the `MovieData` model and includes the following fields:
- `id`
- `name`
- `duration`
- `rating`
- `genre`
- `image`

## ViewSets

### MovieViewSet
This viewset provides CRUD operations for the `MovieData` model.

### DramaMovieViewSet
This viewset filters movies with the genre 'Drama'.

### GenreMovieViewSet
This viewset filters movies based on a genre passed as a path parameter.

## URL Configuration

The URLs are configured using Django's `DefaultRouter`, and the following endpoints are available:
- `/movies/`: List all movies and create a new movie
- `/movies/<id>/`: Retrieve, update, or delete a specific movie
- `/drama/`: List all movies with the genre 'Drama'
- `/genre/<genre>/`: List all movies with the specified genre

## Installation

1. Clone the repository
```bash
git clone https://github.com/chriswilder3/cinemerit.git
cd movies-api
```
2. Install the dependencies
```
pip install -r requirements.txt
```
3. Apply Migrations
```
python manage.py migrate
```
4. Run the Server
```
python manage.py runserver
```
5. Access the API at http://127.0.0.1:8000/

## Acknowledgements
Feel free to modify it according to your needs. If you need further customization, let me know!

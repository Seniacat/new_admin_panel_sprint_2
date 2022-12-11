from django.db.models import Q
from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from movies.models import Filmwork, Person, PersonFilmwork


class PersonSerializer(serializers.SlugRelatedField):    
    class Meta:
        model = Person
        fields = ('full_name',)



class FilmworkSerializer(serializers.ModelSerializer):
    genres = StringRelatedField(many=True, read_only=True)
    actors = serializers.SerializerMethodField()
    directors = serializers.SerializerMethodField()
    writers = serializers.SerializerMethodField()
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'creation_date',
            'rating',
            'type',
            'genres',
            'actors',
            'directors',
            'writers',
        )
        model = Filmwork

    def get_genres(self, movie):
        return movie.genres

    def get_actors(self, movie):
        return movie.actors

    def get_directors(self, movie):
        return movie.directors

    def get_writers(self, movie):
        return movie.writers
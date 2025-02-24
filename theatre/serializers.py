from rest_framework import serializers
from .models import Actor, Genre, Play, Performance, Reservation


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class PlaySerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Play
        fields = '__all__'


class PerformanceSerializer(serializers.ModelSerializer):
    play = PlaySerializer(read_only=True)

    class Meta:
        model = Performance
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    performance = PerformanceSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = '__all__'

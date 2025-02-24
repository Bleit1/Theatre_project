from django.contrib import admin
from .models import Actor, Genre, Play, Performance, Reservation

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('genres', 'actors')

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('play', 'start_time', 'end_time')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('performance', 'user', 'seats')

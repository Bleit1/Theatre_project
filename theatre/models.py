from django.db import models

class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

class Play(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)

    def __str__(self) -> str:
        return self.title

class Performance(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE, related_name='performances')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.play.title} at {self.start_time}"

class Reservation(models.Model):
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE, related_name='reservations')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    seats = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"Reservation by {self.user.email} for {self.performance.play.title}"

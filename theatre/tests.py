from datetime import datetime, timedelta
import pytz

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from theatre.models import Actor, Genre, Play, Performance, Reservation

User = get_user_model()


class ModelStringTests(TestCase):
    def test_actor_str(self):
        actor = Actor.objects.create(first_name="John", last_name="Doe")
        self.assertEqual(str(actor), "John Doe")

    def test_genre_str(self):
        genre = Genre.objects.create(name="Drama")
        self.assertEqual(str(genre), "Drama")

    def test_play_str(self):
        play = Play.objects.create(title="Hamlet", description="A tragedy by Shakespeare")
        self.assertEqual(str(play), "Hamlet")

    def test_performance_str(self):
        play = Play.objects.create(title="Hamlet", description="A tragedy by Shakespeare")
        tz = pytz.UTC
        start_time = datetime.now(tz) + timedelta(days=1)
        end_time = start_time + timedelta(hours=2)
        performance = Performance.objects.create(play=play, start_time=start_time, end_time=end_time)
        expected = f"{play.title} at {start_time}"
        self.assertEqual(str(performance), expected)

    def test_reservation_str(self):
        user = User.objects.create_user(username="testuser", email="test@example.com", password="password123")
        play = Play.objects.create(title="Hamlet", description="A tragedy by Shakespeare")
        tz = pytz.UTC
        start_time = datetime.now(tz) + timedelta(days=1)
        end_time = start_time + timedelta(hours=2)
        performance = Performance.objects.create(play=play, start_time=start_time, end_time=end_time)
        reservation = Reservation.objects.create(performance=performance, user=user, seats=2)
        expected = f"Reservation by {user.email} for {play.title}"
        self.assertEqual(str(reservation), expected)


class APIEndpointTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="password123")

    def test_actor_list_endpoint(self):
        url = reverse("actor-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_play_list_endpoint(self):
        url = reverse("play-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performance_list_endpoint(self):
        url = reverse("performance-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ReservationAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="password123")
        self.genre = Genre.objects.create(name="Tragedy")
        self.actor = Actor.objects.create(first_name="Emma", last_name="White")
        self.play = Play.objects.create(title="Macbeth", description="A tragedy by Shakespeare")
        self.play.genres.add(self.genre)
        self.play.actors.add(self.actor)
        tz = pytz.UTC
        self.start_time = datetime.now(tz) + timedelta(days=2)
        self.end_time = self.start_time + timedelta(hours=3)
        self.performance = Performance.objects.create(play=self.play, start_time=self.start_time,
                                                      end_time=self.end_time)
        self.reservation_list_url = reverse("reservation-list")
        self.reservation_data = {
            "performance": self.performance.id,
            "seats": 2,
            "user": self.user.id
        }

    def test_create_reservation_unauthenticated(self):
        response = self.client.post(self.reservation_list_url, data=self.reservation_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_reservation_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.reservation_list_url, data=self.reservation_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reservation.objects.count(), 1)


class UserModelAPITests(APITestCase):
    def test_create_user(self):
        user = User.objects.create_user(username="testuser", email="test@example.com", password="password123")
        self.assertEqual(user.email, "test@example.com")

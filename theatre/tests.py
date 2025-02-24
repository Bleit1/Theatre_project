from django.test import TestCase
from .models import Actor

class ActorModelTest(TestCase):
    def test_actor_str(self):
        actor = Actor.objects.create(first_name="John", last_name="Doe")
        self.assertEqual(str(actor), "John Doe")

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ActorViewSet, GenreViewSet, PlayViewSet,
                    PerformanceViewSet, ReservationViewSet)

router = DefaultRouter()
router.register(r'actors', ActorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'plays', PlayViewSet)
router.register(r'performances', PerformanceViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

"""URLs for user"""

from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserCreateViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)

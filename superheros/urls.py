from django.urls import path
from .views import SuperHeroViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('super-heros', SuperHeroViewset)
urlpatterns = []    
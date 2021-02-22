from django.urls import path
from .views import CombatViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('combat', CombatViewset)

urlpatterns = []
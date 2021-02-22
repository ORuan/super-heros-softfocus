from django.urls import path
from accounts.views import AccountsViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users', AccountsViewset)

urlpatterns = [
    
]
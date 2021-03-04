from accounts.models import Account
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import SuperHero
from .serializers import SuperHeroSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication

class SuperHeroViewset(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)

    serializer_class = SuperHeroSerializer
    queryset = SuperHero.objects.all()

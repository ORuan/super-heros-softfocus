from rest_framework import viewsets
from .models import Combat
from .serializers import CombatSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class CombatViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)


    queryset = Combat.objects.all()
    serializer_class = CombatSerializer
from rest_framework import viewsets
from .models import Combat
from .serializers import CombatSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication


class CombatViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    queryset = Combat.objects.all()
    serializer_class = CombatSerializer
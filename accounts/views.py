from rest_framework import viewsets
from superheros.models import SuperHero
from .serializers import AccountSerializer
from superheros.serializers import SuperHeroSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from accounts.models import Account
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.permissions import AllowAny

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated



class AccountsViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @action(detail=True, methods=["GET"])
    def super_hero(self, request, pk=None):
        account = self.get_object()
        query_super = SuperHero.objects.filter(account_id=account.id)
        serializer = SuperHeroSerializer(query_super, many=True)
        return Response(serializer.data)


class GetUuidToken(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    #permission_classes = [AllowAny]

    # verificar se o token é igual ao do localstorage
    def list(self, request, token):
        print(self.request)
        token_user = Token.objects.get(key=token)
        user_id = Account.objects.get(id=token_user.user.id).id
        return Response(f"{user_id}")

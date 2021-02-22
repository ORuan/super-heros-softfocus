from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from accounts.models import Account
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import AuthenticationFailed


"""class CustomValidateToken(TokenAuthentication):
    def authenticate_credentials(self, key):
        # user = Account.objects.get(id=self.request.user.id)
        print(key)
        print(Token.objects.get(key=key))
        try:
            pass
            # print(user)
            # token = self.model.objects.select_related('accounts').get(key=key)
        except ObjectDoesNotExist:
            # modify the original exception response
            raise AuthenticationFailed('Conta não existe')

        if not user.is_active:
            # can also modify this exception message
            raise AuthenticationFailed('Usuário não existe ou está inativo')
        return (user, token)"""

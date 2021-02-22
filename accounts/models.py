from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.db.models.signals import post_save   
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
    AbstractBaseUser,
    User,
)

class AccountManager(BaseUserManager):
    def create(self, email, password=None):
        if not email:
            raise ValueError(_("Conta deve ter email"))

        user = self.model(email=self.normalize_email(email), password=make_password(password))
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create(email=self.normalize_email(email), password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):

    username = None

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    avatar = models.ImageField(
        upload_to="static", verbose_name="Imagem", default="none.jpg"
    )
    email = models.EmailField(_("email address"), unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(
        _("staff status"),
        default=False,
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['password']
    objects = AccountManager()

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def has_module_perms(self, app_label):
        return True

#Signals
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        print('Created Token')

post_save.connect(create_auth_token, sender=Account)
from django.db import models
from accounts.models import Account


class SuperHero(models.Model):
    class Meta:
        db_table = "SuperHero"

    """set list of universes
    DC = "DC COMICS"
    MV = "MARVEL"
    UNINVERSE_LIST = [
        (DC, "DC COMICS"),
        (MV, "MARVEL"),
    ]
    """
    universe = models.CharField(max_length=9, blank=False)
    name = models.CharField(verbose_name="name", null=False, max_length=40, unique=True)
    description = models.TextField(
        verbose_name="description", null=False, max_length=100
    )
    stared = models.BooleanField(default=False)
    height = models.IntegerField(null=False)
    weigth = models.IntegerField(null=False)
    speed = models.IntegerField(null=False)
    power = models.FloatField(null=False)
    account_id = models.ForeignKey(
        Account, related_name="accounts", on_delete=models.CASCADE, blank=True, db_constraint=False)
    super_hero_image = models.ImageField(
        upload_to="static", default="none.jpg")

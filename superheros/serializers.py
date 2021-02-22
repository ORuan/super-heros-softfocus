from rest_framework import serializers
from .models import SuperHero
from accounts.serializers import AccountSerializer
from accounts.models import Account


class SuperHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperHero
        extra_kwargs = {'account_id': {'required': False}}
        #fields = '__all__'
        fields = [
            "id",
            "universe",
            "name",
            "description",
            "height",
            "weigth",
            "speed",
            "stared",
            "power",
            "super_hero_image",
            "account_id"
        ]

    def save(self):
        universe = self.validated_data['universe']
        name = self.validated_data['name']
        description = self.validated_data['description']
        height = self.validated_data['height']
        stared = self.validated_data['stared']
        weigth = self.validated_data['weigth']
        speed = self.validated_data['speed']
        power = self.validated_data['power']
        account_id = Account.objects.get(
            email=self.context['request'].user.email)
        self.validated_data['account_id_id'] = account_id.id
        self.instance = self.create(self.validated_data)

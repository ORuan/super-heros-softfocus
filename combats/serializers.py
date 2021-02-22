from rest_framework import serializers
from .models import Combat
from accounts.models import User
from accounts.serializers import AccountSerializer
from accounts.models import Account


class CombatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Combat
        extra_kwargs = {
            'account_id': {'required': False},
            'winner': {'required': False},
            'id': {'read_only': True},
            'a_tie': {'read_only': True},
        }
        fields = [
            "id",
            'first_superhero',
            'second_superhero',
            'account_id',
            'a_tie',
            'winner'
        ]

    def save(self):

        first_superhero = self.validated_data['first_superhero']
        second_superhero = self.validated_data['second_superhero']
        account_id = Account.objects.get(
            email=self.context['request'].user.email)

        self.validated_data['account_id'] = account_id
        self.instance = self.create(self.validated_data)

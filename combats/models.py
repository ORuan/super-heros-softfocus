from django.db import models
import uuid
from accounts.models import Account
from django.utils.timezone import now
from superheros.models import SuperHero


class Combat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    winner = models.ForeignKey(
        SuperHero, on_delete=models.CASCADE, related_name='winner', blank=True, db_constraint=False, null=True)
    account_id = models.ForeignKey(Account, related_name="account_owner",
                                   on_delete=models.CASCADE, blank=True, db_constraint=False)
    first_superhero = models.ForeignKey(
        SuperHero, on_delete=models.CASCADE, related_name='first_superhero')
    second_superhero = models.ForeignKey(
        SuperHero, on_delete=models.CASCADE, related_name='second_superhero')

    a_tie = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        def calculate(data):
            result = []
            for i in range(0, 2):
                result.insert(
                    i, (data['height'][i] * data['weigth'][i]) + (data['speed'][i] + data['power'][i]))

            if result[0] > result[1]:
                response = data['index'][0]

            elif result[0] == result[1]:
                raise ValueError('Os SuperHero Empararam')
            else:
                response = data['index'][1]
            return response

        def define_winner(id_first, id_second):
            """
                O vencedor é decidido com a media arítmética da altura * Peso
                somado a velocidade e poder
            """
            fs = SuperHero.objects.get(id=id_first)
            sd = SuperHero.objects.get(id=id_second)

            data = {
                # Height --> Index 0
                # width --> Index 1
                "index": [
                    id_first,
                    id_second,
                ],
                "height": [
                    fs.height,
                    sd.height
                ],
                "weigth": [
                    fs.weigth,
                    sd.weigth
                ],
                "speed": [
                    fs.speed,
                    sd.speed
                ],
                "power": [
                    fs.power,
                    sd.power
                ],
            }

            return calculate(data)

        try:
            winner_id = define_winner(
                self.first_superhero.id, self.second_superhero.id)
            super_hero_instance = SuperHero.objects.get(id=winner_id)
            self.winner = super_hero_instance
        except ValueError:
            self.a_tie = True
        except Exception as err:
            print(err)
        super(Combat, self).save(*args, **kwargs)

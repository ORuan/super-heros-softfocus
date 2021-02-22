# Generated by Django 3.1 on 2021-02-17 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('superheros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Combat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('account_id', models.ForeignKey(blank=True, db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='account_owner', to=settings.AUTH_USER_MODEL)),
                ('first_superhero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_superhero', to='superheros.superhero')),
                ('second_superhero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_superhero', to='superheros.superhero')),
            ],
        ),
    ]
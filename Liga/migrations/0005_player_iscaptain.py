# Generated by Django 3.2 on 2022-04-04 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Liga', '0004_game_isplayed'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='iscaptain',
            field=models.BooleanField(default=False),
        ),
    ]

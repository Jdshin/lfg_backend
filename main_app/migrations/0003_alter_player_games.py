# Generated by Django 4.0.2 on 2022-03-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_event_name_game_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='games',
            field=models.ManyToManyField(blank=True, related_name='players', to='main_app.Game'),
        ),
    ]
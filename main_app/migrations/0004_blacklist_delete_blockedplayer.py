# Generated by Django 4.0.3 on 2022-03-09 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_player_games'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blacklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blockedUsers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blockedPlayers', to='main_app.player')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='blacklist', to='main_app.player')),
            ],
        ),
        migrations.DeleteModel(
            name='BlockedPlayer',
        ),
    ]

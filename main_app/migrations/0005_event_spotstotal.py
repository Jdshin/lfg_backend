# Generated by Django 4.0.2 on 2022-03-10 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_blacklist_delete_blockedplayer'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='spotsTotal',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

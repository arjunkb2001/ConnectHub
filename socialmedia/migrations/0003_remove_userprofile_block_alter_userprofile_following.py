# Generated by Django 4.2.7 on 2024-02-01 03:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialmedia', '0002_stories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='block',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='following',
            field=models.ManyToManyField(null=True, related_name='followings', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.0 on 2024-06-09 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0004_remove_challenge_is_shared'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProgress',
        ),
    ]
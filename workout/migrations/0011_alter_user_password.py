# Generated by Django 4.0 on 2024-06-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0010_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]

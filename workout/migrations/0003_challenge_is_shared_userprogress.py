# Generated by Django 4.0 on 2024-06-09 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0002_remove_user_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='is_shared',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='UserProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout.challenge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout.user')),
            ],
        ),
    ]

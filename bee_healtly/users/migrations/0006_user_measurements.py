# Generated by Django 4.1.7 on 2023-03-21 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_measurements_remove_user_height_remove_user_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='measurements',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.measurements'),
        ),
    ]
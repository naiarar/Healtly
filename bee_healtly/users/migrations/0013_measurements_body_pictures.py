# Generated by Django 4.1.7 on 2023-03-27 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurements',
            name='body_pictures',
            field=models.ImageField(blank=True, upload_to='users_pictures'),
        ),
    ]
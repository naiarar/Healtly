# Generated by Django 4.1.7 on 2023-03-28 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_user_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
    ]

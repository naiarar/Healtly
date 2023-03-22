# Generated by Django 4.1.7 on 2023-03-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_measurements_measurements_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nivel_treino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intensidade', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='nivel_treino',
            field=models.ManyToManyField(blank=True, to='users.nivel_treino'),
        ),
    ]

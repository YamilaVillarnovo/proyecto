# Generated by Django 4.2.4 on 2023-09-26 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rutina',
            name='nivel_dificultad',
            field=models.CharField(choices=[('leve', 'Leve'), ('moderada', 'Moderada'), ('energica', 'Energica')], max_length=50),
        ),
    ]

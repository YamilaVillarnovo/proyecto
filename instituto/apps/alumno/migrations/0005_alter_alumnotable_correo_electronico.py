# Generated by Django 4.2.4 on 2023-09-26 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0004_alter_alumnotable_correo_electronico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnotable',
            name='correo_electronico',
            field=models.EmailField(max_length=254),
        ),
    ]

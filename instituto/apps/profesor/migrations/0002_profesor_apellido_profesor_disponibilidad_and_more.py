# Generated by Django 4.2.4 on 2023-09-22 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='apellido',
            field=models.CharField(default=100, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesor',
            name='disponibilidad',
            field=models.CharField(default=100, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesor',
            name='especializacion',
            field=models.CharField(default=100, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesor',
            name='nombre',
            field=models.CharField(default=100, max_length=100),
            preserve_default=False,
        ),
    ]

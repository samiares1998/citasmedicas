# Generated by Django 2.1.8 on 2019-05-17 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_auto_20190517_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes'),
        ),
    ]

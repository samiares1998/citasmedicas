# Generated by Django 2.1.8 on 2019-05-17 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0005_auto_20190517_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='email',
            field=models.CharField(max_length=280, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='password',
            field=models.CharField(max_length=280, null=True),
        ),
    ]

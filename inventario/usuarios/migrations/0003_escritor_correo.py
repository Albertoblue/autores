# Generated by Django 3.2.4 on 2021-07-20 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_remove_escritor_correo'),
    ]

    operations = [
        migrations.AddField(
            model_name='escritor',
            name='correo',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]

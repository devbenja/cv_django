# Generated by Django 3.2.21 on 2023-09-11 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0002_habilidades'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
    ]

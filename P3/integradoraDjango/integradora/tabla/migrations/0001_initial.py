# Generated by Django 5.1.2 on 2024-11-29 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('Servicio_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=255)),
                ('Descripcion', models.TextField()),
                ('Costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Activo', models.BooleanField(default=True)),
            ],
        ),
    ]

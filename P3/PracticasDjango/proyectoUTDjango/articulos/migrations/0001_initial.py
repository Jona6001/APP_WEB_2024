# Generated by Django 5.1.2 on 2024-11-26 15:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=250, verbose_name='Desccripcion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Creado el')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Titulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('image', models.ImageField(default='null', upload_to='articles', verbose_name='Imagen')),
                ('public', models.BooleanField(verbose_name='¿Visible?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el ')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('categories', models.ManyToManyField(blank=True, to='articulos.category', verbose_name='Categorias')),
            ],
        ),
    ]

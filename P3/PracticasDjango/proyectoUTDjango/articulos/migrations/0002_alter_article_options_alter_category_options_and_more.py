# Generated by Django 5.1.2 on 2024-11-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_at'], 'verbose_name': 'Articulo', 'verbose_name_plural': 'Articulos'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default='No description available', max_length=255, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='articles', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Actualizado el'),
        ),
    ]

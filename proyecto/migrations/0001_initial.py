# Generated by Django 4.2.7 on 2023-11-15 13:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bebidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Despensa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('biografia', ckeditor.fields.RichTextField()),
                ('fecha_creacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Limpieza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]

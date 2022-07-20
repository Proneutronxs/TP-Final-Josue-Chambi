# Generated by Django 4.0.5 on 2022-07-04 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='clsAcercade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='clsProductoOriginal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('numero', models.IntegerField()),
                ('version', models.CharField(max_length=5)),
                ('documentacion', models.CharField(max_length=40)),
                ('licencia', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('tamaño', models.CharField(max_length=20)),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
    ]
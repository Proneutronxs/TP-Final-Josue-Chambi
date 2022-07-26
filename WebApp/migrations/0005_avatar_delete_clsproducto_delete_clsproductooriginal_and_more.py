# Generated by Django 4.0.5 on 2022-07-11 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebApp', '0004_clspaquetes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='clsProducto',
        ),
        migrations.DeleteModel(
            name='clsProductoOriginal',
        ),
        migrations.DeleteModel(
            name='clsProductos',
        ),
        migrations.AlterField(
            model_name='clspaquetes',
            name='documentacion',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='clspaquetes',
            name='imagen',
            field=models.CharField(max_length=500),
        ),
    ]

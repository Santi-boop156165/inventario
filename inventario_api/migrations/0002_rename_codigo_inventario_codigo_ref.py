# Generated by Django 4.2.6 on 2023-10-31 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventario',
            old_name='codigo',
            new_name='codigo_ref',
        ),
    ]
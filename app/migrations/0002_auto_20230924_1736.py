# Generated by Django 3.2.21 on 2023-09-24 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userproduct',
            name='product',
        ),
        migrations.RemoveField(
            model_name='userproduct',
            name='user',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='UserProduct',
        ),
    ]
# Generated by Django 4.1 on 2022-08-20 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
    ]

# Generated by Django 4.2.13 on 2024-05-28 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='datetime_created',
        ),
        migrations.RemoveField(
            model_name='book',
            name='datetime_modified',
        ),
    ]

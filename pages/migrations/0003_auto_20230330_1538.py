# Generated by Django 3.0.7 on 2023-03-30 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20230330_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='facebook_link',
        ),
        migrations.RemoveField(
            model_name='team',
            name='google_plus_link',
        ),
        migrations.RemoveField(
            model_name='team',
            name='twitter_link',
        ),
    ]

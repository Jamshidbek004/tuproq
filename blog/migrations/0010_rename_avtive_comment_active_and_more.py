# Generated by Django 4.2.3 on 2024-02-19 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='avtive',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='news',
            new_name='products',
        ),
    ]

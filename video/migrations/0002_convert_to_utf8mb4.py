# Generated by Django 3.0.3 on 2020-04-30 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            'ALTER TABLE users CHANGE user_name user_name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;'
        ),
    ]
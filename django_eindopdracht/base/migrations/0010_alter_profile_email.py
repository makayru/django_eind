# Generated by Django 4.1.7 on 2023-04-20 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
# Generated by Django 4.1.7 on 2023-04-20 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_profile_firstname_alter_profile_lastname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
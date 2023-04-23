# Generated by Django 4.1.7 on 2023-04-20 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='FirstName',
            field=models.CharField(default='john', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='LastName',
            field=models.CharField(default='doe', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='BioText',
            field=models.TextField(blank=True, null=True),
        ),
    ]
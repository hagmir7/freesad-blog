# Generated by Django 4.1.5 on 2023-01-11 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freewsad', '0007_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slug'),
        ),
    ]
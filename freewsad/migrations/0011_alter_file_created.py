# Generated by Django 4.1.5 on 2023-01-11 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freewsad', '0010_alter_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date'),
        ),
    ]
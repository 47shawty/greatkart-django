# Generated by Django 3.1 on 2021-09-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20210918_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(blank=True, upload_to='photos/categories'),
        ),
    ]

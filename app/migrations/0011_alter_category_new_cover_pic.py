# Generated by Django 3.2.9 on 2021-12-06 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_category_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category_new',
            name='cover_pic',
            field=models.FileField(upload_to='category/%Y/%m/%d'),
        ),
    ]

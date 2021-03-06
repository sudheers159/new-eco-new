# Generated by Django 3.2.9 on 2021-11-24 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('roll_no', models.IntegerField(unique=True)),
                ('fee', models.FloatField()),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=150)),
                ('is_registered', models.BooleanField()),
            ],
        ),
    ]

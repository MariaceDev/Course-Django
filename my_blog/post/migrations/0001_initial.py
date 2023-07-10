# Generated by Django 4.2.2 on 2023-07-10 10:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('body_text', models.TextField()),
                ('public_date', models.DateTimeField(default=datetime.date(2023, 7, 10))),
                ('rating', models.IntegerField(default=5)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.author')),
            ],
        ),
    ]

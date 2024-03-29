# Generated by Django 4.1.12 on 2023-10-31 06:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 31, 12, 22, 48, 389941)),
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='artworks/')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.artist')),
            ],
        ),
    ]

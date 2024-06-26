# Generated by Django 5.0.4 on 2024-04-19 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=100)),
                ('published_date', models.DateTimeField()),
                ('isbn', models.CharField(max_length=14)),
                ('pages', models.IntegerField()),
                ('summary', models.TextField()),
            ],
        ),
    ]

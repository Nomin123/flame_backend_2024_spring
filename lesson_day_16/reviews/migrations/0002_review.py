# Generated by Django 5.0.4 on 2024-04-22 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=20)),
                ('Date', models.DateTimeField()),
            ],
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-13 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=255)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('rating', models.IntegerField()),
                ('likes', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
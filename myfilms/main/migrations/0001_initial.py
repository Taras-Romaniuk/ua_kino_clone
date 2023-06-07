# Generated by Django 3.2.6 on 2023-03-22 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('film_id', models.AutoField(primary_key=True, serialize=False)),
                ('film_title', models.TextField(blank=True, null=True)),
                ('film_description', models.TextField(blank=True, null=True)),
                ('film_release_year', models.TextField(blank=True, null=True)),
                ('film_country', models.TextField(blank=True, null=True)),
                ('film_genre', models.TextField(blank=True, null=True)),
                ('film_director', models.TextField(blank=True, null=True)),
                ('film_actors', models.TextField(blank=True, null=True)),
                ('film_duration', models.TextField(blank=True, null=True)),
                ('film_imdb_rating', models.TextField(blank=True, db_column='film_IMDb_rating', null=True)),
                ('film_thumb_image', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Films',
                'managed': False,
            },
        ),
    ]

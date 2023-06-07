# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Films(models.Model):
    film_id = models.AutoField(primary_key=True, blank=True, null=False)
    film_title = models.TextField(blank=True, null=True)
    film_description = models.TextField(blank=True, null=True)
    film_release_year = models.TextField(blank=True, null=True)
    film_country = models.TextField(blank=True, null=True)
    film_genre = models.TextField(blank=True, null=True)
    film_director = models.TextField(blank=True, null=True)
    film_actors = models.TextField(blank=True, null=True)
    film_duration = models.TextField(blank=True, null=True)
    # Field name made lowercase.
    film_imdb_rating = models.TextField(
        db_column='film_IMDb_rating', blank=True, null=True)
    film_thumb_image = models.ImageField(upload_to="myfilms/static/media", blank=True)

    class Meta:
        managed = False
        db_table = 'Films'

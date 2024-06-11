# Generated by Django 4.2.13 on 2024-06-10 23:15

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "lat_long",
                    django.contrib.gis.db.models.fields.PointField(
                        default=django.contrib.gis.geos.point.Point(0.0, 0.0),
                        geography=True,
                        srid=4326,
                    ),
                ),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("date_added", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Weather",
            fields=[
                ("weatherID", models.BigAutoField(primary_key=True, serialize=False)),
                ("date", models.DateField()),
                ("tempmax", models.FloatField()),
                ("tempmin", models.FloatField()),
                ("temp", models.FloatField()),
                ("dew", models.FloatField()),
                ("humidity", models.FloatField()),
                ("precip", models.FloatField()),
                ("precipprob", models.FloatField()),
                ("precipcover", models.FloatField()),
                ("preciptype", models.CharField(max_length=100)),
                ("windgust", models.FloatField()),
                ("windspeed", models.FloatField()),
                ("winddir", models.FloatField()),
                ("sunrise", models.CharField(max_length=100)),
                ("sunset", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Hunt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_of_hunt", models.DateField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "total_ducks",
                    models.IntegerField(
                        default=0, help_text=" Total number of ducks taken during hunt."
                    ),
                ),
                (
                    "total_geese",
                    models.IntegerField(
                        default=0, help_text=" Total number of geese taken during hunt."
                    ),
                ),
                ("photo_url", models.URLField()),
                (
                    "location",
                    django.contrib.gis.db.models.fields.PointField(
                        default=django.contrib.gis.geos.point.Point(0.0, 0.0),
                        geography=True,
                        srid=4326,
                    ),
                ),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("weather_id", models.IntegerField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

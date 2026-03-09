from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2025)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    genre = models.fields.CharField(choices=Genre.choices, max_length=5)

    def __str__(self):
        return f"{self.name}"


class Listing(models.Model):
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=400)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True, blank=True, validators=[MinValueValidator(1900), MaxValueValidator(2025)])

    class Type(models.TextChoices):
        records = 'R'
        clothing = 'C'
        posters = 'P'
        miscellaneous = 'M'
    type = models.fields.CharField(choices=Type.choices, max_length=2)

    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
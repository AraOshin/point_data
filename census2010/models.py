from django.contrib.gis.db import models

class BlockGroup(models.Model):
    state = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    tract =models.CharField(max_length=50)
    tract_no = models.IntegerField() #real type 
    bg = models.CharField(max_length=50)
    trbg = models.CharField(max_length=50)
    fips = models.CharField(max_length=50, primary_key = True)
    pop10 = models.IntegerField()
    du10 = models.IntegerField()
    vac10 = models.IntegerField()
    white = models.IntegerField()
    black = models.IntegerField()
    aian = models.IntegerField()
    asian = models.IntegerField()
    nhpi = models.IntegerField()
    other_race = models.IntegerField()
    pop_2_race = models.IntegerField()
    hispanic = models.IntegerField()
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.fips
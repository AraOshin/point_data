from django.contrib.gis.db import models

class NeighborhoodBoundaries(models.Model):
    objectid = models.IntegerField(primary_key=True )
    name = models.CharField(max_length=75)
    commplan = models.CharField(max_length=50)
    shared = models.CharField(max_length=50)
    coalit = models.CharField(max_length=50)
    horz_vert = models.CharField(max_length=50)
    shape_length = models.FloatField()
    maplabel = models.CharField(max_length=75)
    geom = models.MultiPolygonField(srid=4326)

    # Returns the string representation of the model.
    def __str__(self):
        return self.maplabel
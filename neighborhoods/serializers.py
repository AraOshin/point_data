from rest_framework import serializers
from neighborhoods.models import NeighborhoodBoundaries

class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeighborhoodBoundaries 
        fields = (
          'objectid',
          'name',
          'commplan',
          'shared',
          'coalit',
          'horz_vert',
          'shape_length',
          'maplabel',
          'geom')

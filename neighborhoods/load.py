import os
from django.contrib.gis.utils import LayerMapping
from neighborhoods.models import NeighborhoodBoundaries

neighborhoodboundaries_mapping = {
    'objectid' : 'OBJECTID',
    'name' : 'NAME',
    'commplan' : 'COMMPLAN',
    'shared' : 'SHARED',
    'coalit' : 'COALIT',
    'horz_vert' : 'HORZ_VERT',
    'shape_length' : 'Shape_Length',
    'maplabel' : 'MAPLABEL',
    'geom' : 'MULTIPOLYGON',
}
neighborhood_boundaries_geojson = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Neighborhood_Boundaries.geojson'),
)

def run(verbose=True):
    lm = LayerMapping(
        NeighborhoodBoundaries, neighborhood_boundaries_geojson, neighborhoodboundaries_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)


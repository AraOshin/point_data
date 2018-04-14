import os
from django.contrib.gis.utils import LayerMapping
from .models import BlockGroup

blockgroup_mapping = {
    'state' : 'STATE',
    'county' : 'COUNTY',
    'tract' : 'TRACT',
    'tract_no' : 'TRACT_NO',
    'bg' : 'BG',
    'trbg' : 'TRBG',
    'fips' : 'FIPS',
    'pop10' : 'POP10',
    'du10' : 'DU10',
    'vac10' : 'VAC10',
    'white' : 'WHITE',
    'black' : 'BLACK',
    'aian' : 'AIAN',
    'asian' : 'ASIAN',
    'nhpi' : 'NHPI',
    'other_race' : 'OTHER_RACE',
    'pop_2_race' : 'POP_2_RACE',
    'hispanic' : 'HISPANIC',
    'mpoly' : 'MULTIPOLYGON',
}

census2010_geojson = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'blockgroup2010.geojson'),
)

def run(verbose=True):
    lm = LayerMapping(
        BlockGroup, census2010_geojson, blockgroup_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)


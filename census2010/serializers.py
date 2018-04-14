from rest_framework import serializers
from census2010.models import BlockGroup

class BlockGroup2010Serializer(serializers.ModelSerializer):
    class Meta:
        model = BlockGroup 
        fields = ('state',
    'county',
    'tract',
    'tract_no',
    'bg',
    'trbg',
    'fips',
    'pop10',
    'du10',
    'vac10',
    'white',
    'black',
    'aian',
    'asian',
    'nhpi',
    'other_race',
    'pop_2_race',
    'hispanic',
    'mpoly')

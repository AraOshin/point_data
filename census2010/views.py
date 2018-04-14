from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from census2010.models import BlockGroup
from census2010.serializers import BlockGroup2010Serializer
import json
from django.contrib.gis.geos import Point



@api_view(['GET'])
def blockgroup_detail(request, pk, format=None):

    try:
        block_group = BlockGroup.objects.get(pk=pk)
    except BlockGroup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
            serializer = BlockGroup2010Serializer(block_group)
            return Response(serializer.data)

@api_view(['GET'])
def blockgroup_latlong(request, latlong, format=None):
    if request.method == 'GET':
        # latlong = request.GET['latlong'] #122.628, 45.561
        lat,lon = latlong.split(',')
        pnt = Point(float(lat), float(lon))
        fips = BlockGroup.objects.get(mpoly__intersects=pnt) #fips
        print(fips)
        block_group = BlockGroup.objects.get(pk=fips)
        serializer = BlockGroup2010Serializer(block_group)
        return Response(serializer.data)


# @api_view(['GET'])
# def blockgroup_list(request, format=None):

#     # if request.method == 'GET':
#     #     blockgroups = BlockGroup.objects.all()
#     #     serializer = BlockGroup2010Serializer(blockgroups, many=True)
#     #     return Response(serializer.data)

# 

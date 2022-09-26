from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from super_types.models import SuperType
from super_types.serializers import SuperTypeSerializer
from supers.serializers import SuperSerializer
from .models import Super

# Create your views here.
@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        super_type = request.query_params.get('super_type')
        print(super_type)

        supers = Super.objects.all()
        
        if super_type:
            supers = supers.filter(super_type__type=super_type)
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def heroes_and_villains(request):
    heros = Super.objects.all().filter(super_type__type ='Hero')
    villains = Super.objects.all().filter(super_type__type ='Villain')

    hero_serializer = SuperSerializer(heros, many=True)
    villain_serializer = SuperSerializer(villains, many=True)

    super_resp_dict = {
        'Heros': hero_serializer.data,
        'Villains': villain_serializer.data
    }

    return Response(super_resp_dict)
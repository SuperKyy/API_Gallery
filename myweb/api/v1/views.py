from django.shortcuts import render

# # Create your views here.
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# from apps.dashboard.models import Item
# from .serializers import ItemSerializer
# @api_view(['GET'])
# def item_list(request):
#     items = Item.objects.all()
#     serializer = ItemSerializer(items, many=True)
#     return JsonResponse(serializer.data, safe=False)
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.dashboard.models import Gallery
from api.v1.serializers import GallerySerializer
import requests


class GalleryViewset(ModelViewSet):
    if requests.method == "POST":
        data = requests.data
        serializer = GallerySerializer(data=data)
        if serializer.is_valid():
            Gallery = serializer.save()
            data = serializer.data
            return Response(data=data)
        return Response(serializer.errors, status=400)
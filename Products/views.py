from django.shortcuts import render
from rest_framework import generics
from .models import Item
from .serializers import CategorySerializers,ItemSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class CategoryCreate(generics.CreateAPIView):
    serializer_class=CategorySerializers
    
    
class ItemCreate(generics.CreateAPIView):
    serializer_class=ItemSerializers
    
class ItemDetail(generics.RetrieveAPIView):
    queryset= Item.objects.all()
    serializer_class=ItemSerializers
    
    
@api_view(['GET'])
def items(request):
    objects= Item.objects.all()
    serializer= ItemSerializers(objects,many=True)
    return Response({"data":serializer.data})
    
    

    



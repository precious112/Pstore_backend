from .models import Category,Item
from rest_framework import serializers

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('category')

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model=Item 
        fields=('id','item_category','item_name','item_image','item_price','about_item')
        

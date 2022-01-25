from django.db import models
from django.utils import timezone
from PIL import Image

# Create your models here.

class Category(models.Model):
    category=models.CharField(max_length=100)
    
    def _str_(self):
        return self.category
    
class Item(models.Model):
    item_category= models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name= models.CharField(max_length=100)
    item_image=models.ImageField(upload_to='media')
    item_price= models.CharField(max_length=100)
    about_item= models.TextField()
    
    def _str_(self):
        return self.item_name 
    
from django.urls import path
from .views import CategoryCreate,ItemCreate,ItemDetail,items

urlpatterns=[
    path('<int:pk>/', ItemDetail.as_view(),name='detailcreate'),
    path('', items,name='listcreate'),
    path('item/create', ItemCreate.as_view(),name='listcreate'),
    path('category/create', CategoryCreate.as_view(),name='listcreate'),
    
 ]
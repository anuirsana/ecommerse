from django.contrib import admin
from django.urls import path,include

from cartapp import views

app_name='cartapp'

urlpatterns=[
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('',views.Cartdetail,name="cartdetail"),
    path( 'remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path( 'full_remove/<int:product_id>/',views.full_remove,name='full_remove')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_toko, name='home_toko'),
    path('new_post', views.input_post, name='input_post'),
    path('barang/<int:post_id>/', views.post_detail, name="post_detail")
]

from django.urls import path
from . import views
urlpatterns = [
    path('',views.more,name='more'),
    path('uploads/',views.upload_image,name='upload_img'),
]

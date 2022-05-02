from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index-2/',views.index_2,name='index-2'),
    path('index-3/',views.index_3,name='index-3'),
    path('index-4/',views.index_4,name='index-4'),
]

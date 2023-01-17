from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.root,name="root" ),
    path('apidata/',views.home,name="home" ),
]
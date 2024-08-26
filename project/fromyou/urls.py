from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',ragister_views,name='ragister'),
    path('login',login_views,name='login')
    
]

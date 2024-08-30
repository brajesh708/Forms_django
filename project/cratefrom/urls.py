# from django.urls import path
# from .views import *
# from cratefrom import views

# urlpatterns = [
#     path('',home,name='home'),
#     path("login/",login,name='login')
# ]
from django.contrib import admin
from django.urls import path
from cratefrom import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path("login/",views.login,name='login')
]
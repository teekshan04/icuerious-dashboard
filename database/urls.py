from django.contrib import admin
from django.urls import path
from . import views
appname= "database"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    #path('importer/', views.importer, name='importer')
   # path('', views.importer, name='importer'),
    path('dashboard1/',views.dashboard1,name='dashboard1'),
    #path('testing/',views.testing,name='testing'),
    path('home/', views.home,name='home'),
    path('home1/', views.home1,name='home1'),
    path('check/', views.check, name="check"),
    path('check1/', views.check1, name="check1"),
    path('home0/', views.home0, name="home0"),
   # path('your_handler/',views.your_handler,name="your_handler"),
   # path('checking/', views.checking, name="checking")
]
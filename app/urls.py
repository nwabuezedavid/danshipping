from django.urls import path
from .views import *
urlpatterns=[
      path('', home, name='home'),
      path('about-us/', about , name='about'),
      path('air-freight/', airposrt , name='airposrt'),
      path('export/', export , name='export'),
      path('ourclient/', ourclient , name='ourclient'),
      path('import/', importx , name='importx'),
      path('Truck-Load/', TruckLoad , name='TruckLoad'),
      path('TRACKINGRESULT/<pk>/', TRACKINGRESULT , name='TRACKINGRESULT'),
      path('SeaFreight/', SeaFreight , name='SeaFreight'),
      path('Requestforquote/', Requestforquote , name='Requestforquote'),
      path('SeawaveLogistics/', SeawaveLogistics , name='SeawaveLogistics'),
      path('ContactheretoAdministrator/', ContactheretoAdministrator , name='ContactheretoAdministrator'),
      path('CustomsBrokerage/', CustomsBrokerage , name='CustomsBrokerage'),
      path('auth-central/<pk>/', adminb , name='adminb'),
      path('Auth/', auth , name='auth'),
      path('logout-admin/', logoutUser , name='logoutUser'),
      path('fetch/', fetch , name='fetch'),
      path('fetchone/<pk>/', fetchone , name='fetchone'),
]
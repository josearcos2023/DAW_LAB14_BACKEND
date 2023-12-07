from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('empleados',views.TrabajadoresView.as_view(),name='empleados'),
]

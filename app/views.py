from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Trabajador
from .serializer import TrabajadorSerializer

class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)

class TrabajadoresView(APIView):
    
    def get(self,request):
        dataTrabajadores = Trabajador.objects.all()
        serTrabajadores = TrabajadorSerializer(dataTrabajadores,many=True)
        return Response(serTrabajadores.data)
    
    def post(self,request):
        serTrabajador = TrabajadorSerializer(data=request.data)
        serTrabajador.is_valid(raise_exception=True)
        serTrabajador.save()
        
        return Response(serTrabajador.data)


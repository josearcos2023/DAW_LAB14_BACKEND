from rest_framework.serializers import ModelSerializer
from .models import Trabajador

class TrabajadorSerializer(ModelSerializer):
    class Meta:
        model = Trabajador
        fields = ('id','nombre', 'categoria', 'horas_trabajadas','pago')

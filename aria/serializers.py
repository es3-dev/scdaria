from rest_framework import serializers
from .models import Sede, Reunion, Asistencia

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'

class ReunionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reunion
        fields = '__all__'

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'

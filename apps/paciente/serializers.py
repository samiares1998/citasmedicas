from rest_framework import serializers

from apps.paciente.models import  (
    cita, Paciente,
)


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('nombres','usuario','password','email') 


class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = cita
        fields = ('nombrePaciente','correo','fecha_creacion','motivo','especialista','paciente') 


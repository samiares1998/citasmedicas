from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



class Paciente(models.Model):
	id = models.AutoField(primary_key=True)
	#paciente = models.OneToOneField(User, on_delete=models.CASCADE)
	usuario = models.CharField(max_length=280, null=True)
	nombres = models.CharField(max_length=280, null=True)
	password = models.CharField(max_length=280, null=True)
	email = models.CharField(max_length=280, null=True)




class cita(models.Model):
	
	id = models.AutoField(primary_key=True)
	nombrePaciente = models.CharField(max_length = 200,blank=False,null=False) #aca se define los atributos de la tabla , si va nulo o si es blanco
	correo = models.CharField(max_length = 200,blank=False,null=False)
	fecha_creacion = models.DateField(default=timezone.now)
	motivo = models.TextField()
	especialista = models.CharField(max_length = 200,blank=False,null=False)
	imagen = models.ImageField(upload_to = 'imagenes',null=True)
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "cita"
		verbose_name_plural = "citas"
			

	def __str__(self):
		return self.nombrePaciente











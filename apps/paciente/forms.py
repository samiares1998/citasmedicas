from django import forms
from .models import Paciente
from django.contrib.auth.models import User

class PacienteForm(forms.ModelForm): #esta clase recive todo por ehrencia 
	
	class Meta: #esto nos ahorra codigo 
		model = Paciente
		fields = ['nombres','usuario','password','email'] #hacemos referencias a los campos que tenemos en el modelo
		




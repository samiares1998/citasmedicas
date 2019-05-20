from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
#from .forms import SignUpForm,UserForm,ProfileForm
from django.contrib.auth.forms import UserCreationForm
from .models import cita,Paciente
# Create your views here.
from django.utils import timezone
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .forms import PacienteForm
from rest_framework import generics
from .serializers import PacienteSerializer,CitaSerializer
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.conf import settings
from django.core import mail

def Home(request):
	#user = UserForm(instance=request.user)
	request.session['email'] = 0
	request.session['name'] = 0
	request.session['id'] = 0

	return render(request,'index/index.html') #{'user':user}carpeta y archivo


def Registro(request):
	if request.method == 'POST':
		bEmail = Paciente.objects.filter(email=request.POST['email']).first()
		busuario = Paciente.objects.filter(usuario=request.POST['usuario']).first()
		print("emaellll",bEmail)
		if (bEmail == None and busuario == None):
			c = Paciente.objects.create(usuario = request.POST['usuario'])
			c.nombres = request.POST['nombres']
			c.password = request.POST['password']
			c.email = request.POST['email']
			c.save()
			request.session['email'] = c.email
			request.session['name'] = c.nombres
			request.session['id'] = c.id


			
			return redirect('inicio')
		else:
			return redirect('home')

	



	#		form.save()
	#		username = form.cleaned_data.get('username')
	#		raw_password = form.cleaned_data.get('password1')
	#		user = authenticate(username=username, password=raw_password)
	#		login(request, user)
	#		return redirect('inicio')

	#else:
	return redirect('home')

        
	





 

def BienvenidaView(request):
	print(request.session['id'])

	if request.session['id'] != 0:
		return render(request,'usuario/home.html') #carpeta y archivo
	else:
		return redirect('home')




def añadir(request):
	if request.session['id'] != 0:
		return render(request,'usuario/añadir.html')
	else:
		return redirect('home')
	




#@login_required
def registroCitas(request):

	#connection = mail.get_connection()
	#connection.open()
	if request.session['id'] != 0:
		if request.method == 'POST':

			nombrePaciente = request.POST['name']
			a=request.FILES.get('imagen', False)
			id1=request.session['id']

			c = cita.objects.create(paciente = Paciente.objects.get(id = id1))

			c.nombrePaciente = request.POST['name']
			c.correo = request.POST['correo']
			c.motivo = request.POST['descripcion']
			c.especialista = request.POST['especialista']
			from_email = settings.EMAIL_HOST_USER
			to_email = [from_email , request.POST['correo']]
			if (a != False):
				c.imagen = request.FILES['imagen']

			c.save()
			mail = request.POST['correo']
			print(type(mail)) 
			print("pruebaaa",request.POST['correo'])

			email_message = EmailMessage(
				"cita Registrada",
				"Registro exitoso",
				settings.EMAIL_HOST_USER,
				[mail],
				)
			email_message.content_subtype = 'html'
			email_message.send()
		

			

			return redirect('listarCitas')
		else:
			return redirect('home')



def listarCitas(request):
	if request.session['id'] != 0:
		id1=request.session['id']
		citas = cita.objects.filter(paciente=id1)
		#request.session['0']
		return render(request,'usuario/listar.html',{'citas':citas})
	else:
			return redirect('home')


def eliminar(request,id):
	if request.session['id'] != 0:
		citad = cita.objects.get(id = id)
		citad.delete()
		return redirect('listarCitas')
	else:
		return redirect('home')



def login(request):
	if request.method == 'POST':
	    email = request.POST['email']
	    password = request.POST['password']
	    conf = Paciente.objects.filter(email=email,password=password)
	    print("Holaaa",conf)
	    if conf:
	    	request.session['email'] = email
	    	request.session['name'] = conf[0].usuario
	    	request.session['id'] = conf[0].id
	    	return redirect('inicio')

	        
	    else:
	        return redirect('home')




def terminar(request):
	request.session['email'] = 0
	request.session['name'] = 0
	request.session['id'] = 0
	return redirect('home')



class pacienteList(generics.ListCreateAPIView): #para poder acceder al metodo get y post
	queryset = Paciente.objects.all()
	serializer_class = PacienteSerializer




class pacienteDetail(APIView): #para poder acceder al metodo update,delete
	
	def get(self, request, pk, format=None):
		p = Paciente.objects.filter(id=pk)
		c = cita.objects.filter(paciente=p[0]).all()
		serializer = PacienteSerializer(c, many=True)
		return Response(serializer.data)
#modelos del nucleo de django
from django.shortcuts import render
from django.views.generic import View
#modelos propios
from django.contrib.auth.models import User

#Vista para la creacion de un usuario
class CreateUserView(View):

    def get(self,request):
        return render(request,'profiles/create_user.html')

#Vista para el login de un usuario
class LoginUserView(View):

    def get(self,request):
        return render(request,'profiles/login_user.html')
        

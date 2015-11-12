#modelos del nucleo de django
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
#modelos propios
from .forms import CreateUserForm


#Vista para la creacion de un usuario
class CreateUserView(View):

    def get(self,request):
        return render(request,'profiles/create_user.html',{'form':CreateUserForm})

    def post(self,request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                request.POST['username'],
                request.POST['email'],
                request.POST['password'])
            user.save()
            return render(request,'profiles/login_user.html')



#Vista para el login de un usuario
class LoginUserView(View):

    def get(self,request):
        return render(request,'profiles/login_user.html')

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Usuario Logeado')

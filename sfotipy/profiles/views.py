#modelos del nucleo de django
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
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

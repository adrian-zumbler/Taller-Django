from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User

class CreateUserView(View):

    def get(self,request):
        return render(request,'profiles/create_user.html')

class LoginUserView(View):

    def get(self,request):
        return render(request,'profiles/login_user.html')        

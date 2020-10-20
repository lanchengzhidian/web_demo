from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from users.models import User


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create(username=username, password=password)
        return HttpResponse("<h1>注册成功<h1>")

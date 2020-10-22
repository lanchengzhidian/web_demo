from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, JsonResponse
from users.models import User


def register(request):
    if request.method == 'GET':  # --> GET方式

        return render(request, 'register.html')

    else:  # --> POST方式
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create(username=username, password=password)

        # return HttpResponse('<h1>注册成功</h1>')  --> 返回html页面
        # return JsonResponse({'message': '注册成功'})  --> 返回Json数据
        return redirect('/login/')  # --> 页面重定向, 返回登录页面


def login(request):
    """登录View视图函数"""
    if request.method == 'GET':  # --> GET方式
        username = request.COOKIES.get('username')

        return render(request, 'login.html', context={'username': username})

    else:  # --> POST方式
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return JsonResponse({'message': 'login failed'})
        else:
            response = JsonResponse({'message': 'login success'})
            if remember == 'true':
                response.set_cookie('username', username, max_age=3600)
            return response


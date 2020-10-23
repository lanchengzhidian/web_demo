from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, JsonResponse
from users.models import User
from django.views import View


# def register(request):
#     if request.method == 'GET':  # --> GET方式
#
#         return render(request, 'register.html')
#
#     else:  # --> POST方式
#         import json
#         req_dict = json.loads(request.body)
#         username = req_dict.get('username')
#         password = req_dict.get('password')
#         print(f'username: {username}, password: {password}')
#         user = User.objects.create(username=username, password=password)
#         return HttpResponse('注册成功')
#
#
# def login(request):
#     """登录View视图函数"""
#     username = request.session.get('username')
#     if username:
#         return HttpResponse(f'{username}用户已登录')
#     if request.method == 'GET':  # --> GET方式
#         return render(request, 'login.html')
#
#     else:  # --> POST方式
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         remember = request.POST.get('remember')
#         try:
#             user = User.objects.get(username=username, password=password)
#         except User.DoesNotExist:
#             return JsonResponse({'message': 'login failed'})
#         else:
#             request.session['user_id'] = user.id
#             request.session['username'] = user.username
#             if remember != 'true':
#                 request.session.set_expiry(0)
#             return JsonResponse({'message': 'login success'})
def register(request):
    if request.method == 'GET':  # --> GET方式

        return render(request, 'register.html')

    else:  # --> POST方式
        import json
        req_dict = json.loads(request.body)
        username = req_dict.get('username')
        password = req_dict.get('password')
        print(f'username: {username}, password: {password}')
        user = User.objects.create(username=username, password=password)
        return HttpResponse('注册成功')


class LoginView(View):
    """登录类视图"""
    def get(self, request):
        """获取登录界面"""
        username = request.session.get('username')
        if username:
            return HttpResponse(f'{username}用户已登录')
        if request.method == 'GET':  # --> GET方式
            return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return JsonResponse({'message': 'login failed'})
        else:
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            if remember != 'true':
                request.session.set_expiry(0)
            return JsonResponse({'message': 'login success'})


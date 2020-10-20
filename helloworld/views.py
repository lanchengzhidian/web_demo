from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def first_view_func(request):
    return HttpResponse('<h1>hello world</h1>')


def second_view_func(request):
    return HttpResponse('<h2>Hello Python</h2>')

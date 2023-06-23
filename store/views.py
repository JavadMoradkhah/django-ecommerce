from django.shortcuts import render
from django.http.request import HttpRequest


def home(request: HttpRequest):
    return render(request, 'index.html')

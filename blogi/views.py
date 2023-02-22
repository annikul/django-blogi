from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def postaukset(request):
    return HttpResponse('Moi!')

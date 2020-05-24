from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

import re

from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.urls import reverse
from .forms import LoginForm, RegistrationForm
from .models import EmailConfirmed

def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out.")
    return HttpResponseRedirect('%s'%(reverse("accounts:auth_login")))


def login_view(request):
    form = LoginForm(request.POST or None)
    btn = "Login"
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, "Successfully logged in. Welcome back!")
        return HttpResponseRedirect("/")
    context = {
        "form": form,
        "submit_btn": btn
    }
    return render(request, "form.html", context)


def registration_view(request):
    form = RegistrationForm(request.POST or None)
    btn = "Join"
    if request.method == "POST" and form.is_valid():
        new_user = form.save(commit=False)
        # form.cleaned_data['password1']
        new_user.save()
        messages.success(request, "Successfully registered. Please check your email for confirmation.")
        return HttpResponseRedirect("/")
    context = {
        "form": form,
        "submit_btn": btn
    }
    return render(request, "form.html", context)


SHA1_RE = re.compile('^[a-f0-9]{40}$')
def activation_view(request, activation_key):
    if SHA1_RE.search(activation_key):
        print("activation key is real")
        try:
            instance = EmailConfirmed.objects.get(activation_key=activation_key)
        except EmailConfirmed.DoesNotExist:
            messages.success(request, "There was an error with your request")
            instance = None
            raise HttpResponseRedirect("/")

        if instance is not None and not instance.confirmed:
            page_message = "Confirmation successful! Welcome."
            instance.confirmed = True
            instance.activation_key = "Confirmed"
            instance.save()
            messages.success(request, "Successfully confirmed. Please login!")
        elif instance is not None and instance.confirmed:
            page_message = "Already confirmed"
            messages.success(request, "Already confirmed.!")
        else:
            page_message = ""
            pass

        context = {"page_message": page_message}
        return render(request, "accounts/activation_complete.html", context)
    else:
        raise Http404
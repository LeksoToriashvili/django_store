from http.client import HTTPResponse

from django.contrib.auth import get_user_model, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView
from django.contrib import messages

from core.forms import UserRegistrationForm
from django_store.settings import AUTH_USER_MODEL


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


class RegisterView(CreateView):
    template_name = 'register.html'
    model = get_user_model()
    form_class = UserRegistrationForm
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)

        user = form.save()
        login(self.request, user)

        return response

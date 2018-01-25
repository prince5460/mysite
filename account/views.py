from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse


def user_login(request):
    return None


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:blog_title'))
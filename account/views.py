from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def user_login(request):
    return None


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:blog_title'))


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('blog:blog_title'))

    context = {'form': form}
    return render(request, 'account/register.html', context)

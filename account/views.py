from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from .forms import LoginForm, RegistrationForm, UserProfileForm


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                login(request, user)
                return HttpResponse('Welcome.You have been authenticated successfully.')
            else:
                return HttpResponse('Sorry,your username or password is not right.')
        else:
            return HttpResponse('Invalid login.')

    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'account/login.html', {'form': login_form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:blog_title'))


# def register(request):
#     if request.method != 'POST':
#         form = UserCreationForm()
#     else:
#         form = UserCreationForm(data=request.POST)
#
#         if form.is_valid():
#             new_user = form.save()
#             authenticated_user = authenticate(username=new_user.username,
#                                               password=request.POST['password1'])
#             login(request, authenticated_user)
#             return HttpResponseRedirect(reverse('blog:blog_title'))
#
#     context = {'form': form}
#     return render(request, 'account/register.html', context)

def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponse('Successfully!')
        else:
            return HttpResponse('Sorry,you can not register.')
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, 'account/register.html', {'form': user_form, 'profile': userprofile_form})

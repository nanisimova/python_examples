from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from user.forms import UserUpdateForm
from catalog.models import Catalog

# Создание пользователя, просмотр профиля, обновление, удаление и смена пароля

def create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 == password2:
                user = User.objects.create_user(username, password=password1)
                return HttpResponseRedirect('/')

    form = UserCreationForm()

    return render(request, 'user/create.html', {'form': form })


def view(request):
    if request.user.is_authenticated:
        items = Catalog.objects.filter(user_id = request.user.id, is_active = 1)
        return render(request, 'user/view.html', { 'items': items.values_list() })
    else:
        return HttpResponseRedirect('/auth/login')


def update(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        if request.method == 'POST':
            form = UserUpdateForm(request.POST)
            if form.is_valid():

                user.last_name = form.cleaned_data['last_name']
                user.first_name = form.cleaned_data['first_name']
                user.email = form.cleaned_data['email']
                user.save()

        form = UserUpdateForm(initial={'first_name': user.first_name,
            'last_name': user.last_name, 'email': user.email})
        return render(request, 'user/update.html', {'form': form })
    else:
        return HttpResponseRedirect('/auth/login')


def delete(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        user.is_active = 0

        user.save()
        return HttpResponseRedirect('/auth/logout')
    else:
        return HttpResponseRedirect('/auth/login')



def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pass1 = request.POST['new_password1']
            pass2 = request.POST['new_password2']
            pass_old = request.POST['old_password']
            if pass1 == pass2:
                user = User.objects.get(username=request.user.username)
                user.set_password(pass2)
                user.save()

        form = PasswordChangeForm(request.user)
        return render(request, 'user/change_password.html', {'form': form })
    else:
        return HttpResponseRedirect('/auth/login')


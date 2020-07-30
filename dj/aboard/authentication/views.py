from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm


def auth_login(request):

    if not request.user.is_authenticated:
        params = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                params['error'] = 'invalid_user'
        else:
            params['form'] = AuthenticationForm()

        return render(request, 'auth/login.html', params)
    else:
        return HttpResponseRedirect("/")


def auth_logout(request):
    logout(request)
    # Do something with `template_response`
    return render(request, 'auth/logout.html')



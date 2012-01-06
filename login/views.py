from django.contrib.auth import authenticate, login, logout


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            HttpResponse("You're logged in.")
            # Redirect to a success page.
        else:
            pass
            # Return a 'disabled account' error message
    else:
        HttpResponse("Your username and password didn't match.")


def logout_view(request):
    logout(request)
    # Redirect to a success page.

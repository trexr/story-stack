from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Two example views. Change or delete as necessary.


def home(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # User has specified valid credentials, have user log-in, and then
            # redirect back home
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'pages/home.html', context)


def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)


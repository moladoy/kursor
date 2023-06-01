from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from app.form import CreateUserForm
# Create your views here.
from django.views.generic import ListView

from app.models import Product


class IndexVIew(ListView):
    model = Product
    template_name = 'index.html'
    paginate_by = 6
    queryset = Product.objects.all()


class ProductView(ListView):
    model = Product
    template_name = 'products.html'
    queryset = Product.objects.all()


def about(request):

    return render(request, 'about.html')


def contact(request):

    return render(request, 'contact.html')



def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password incorrect')

    context = {}

    return render(request, 'registration/login.html', context)
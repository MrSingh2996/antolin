from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .models import Customer, ModelData
from django.core.paginator import Paginator

def search_customers(request):
    query = request.GET.get('q')
    if query:
        customers = Customer.objects.filter(name__startswith=query)
    else:
        customers = Customer.objects.all()
    return render(request, 'myapp/search_results.html', {'customers': customers})

def model_data_list(request):
    model_data = ModelData.objects.all()
    paginator = Paginator(model_data, 15)  # Show 15 records per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'myapp/model_data_list.html', {'page_obj': page_obj})

def home(request):
    return render(request, 'myapp/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})

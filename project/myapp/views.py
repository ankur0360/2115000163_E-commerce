from django.shortcuts import render
from .forms import ProductForm
from .models import Products
# Create your views here.

def home(request):
    return render(request, 'base.html')

def Products_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'products.html', context)

def catagories(request):
    products_data = Products.objects.all()
    main_data = {'cata':products_data}
    return render(request,'catagories.html',{"cata":main_data})
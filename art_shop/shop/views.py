from django.shortcuts import render
from .models import Category, User, Product

def index(request):
    categories = [i.name for i in Category.objects.all()]
    return render(request, template_name='artima/index.html')

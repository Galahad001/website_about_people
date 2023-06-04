from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    people =People.objects.all()
    cats = Category.objects.all()
    context = {'people':people, 'cats':cats}
    return render(request, 'people/index.html', context)

def businessman(request, p_id):
    people =People.objects.filter(cat_id=p_id)
    cats = Category.objects.all()
    context = {'people':people, 'cats':cats, 'test_id':p_id}
    return render(request, 'people/businessman.html', context)
# Create your views here.

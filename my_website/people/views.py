from django.shortcuts import render
# from django.http import HttpResponse
from .models import People
from .models import Category
from .serializers import PeopleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_peoples(request):
    if request.method == 'GET':
        peoples = People.objects.all()
        serilizers = PeopleSerializer(peoples, many=True)
        return Response(serilizers.data)
    

@api_view(['GET'])
def api_people_detail(request, pk):
    if request.method == 'GET':
        peoples = People.objects.get(pk=pk)
        serilizers = PeopleSerializer(peoples)
        return Response(serilizers.data)



def index(request):
    people =People.objects.all()
    cats = Category.objects.all()
    context = {'people':people, 'cats':cats}
    return render(request, 'people/index.html', context)
    
def our_way(request):
    return render(request, 'people/our_way.html')

def contacts(request):
    return render(request, 'people/contacts.html')

def questions(request):
    return render(request, 'people/questions.html')

def businessman(request, p_id):
    people =People.objects.filter(cat_id=p_id)
    cats = Category.objects.all()
    context = {'people':people, 'cats':cats, 'test_id':p_id}
    return render(request, 'people/businessman.html', context)
# Create your views here.

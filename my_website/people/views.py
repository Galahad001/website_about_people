from django.shortcuts import redirect, render
from django.urls import reverse_lazy
# from django.http import HttpResponse
from .models import People
from .models import Category
from .serializers import PeopleSerializer
from .forms import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.generic import ListView, CreateView


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


class PeopleCategory(ListView):
    model = Category
    template_name = 'people/index.html'
    context_object_name = 'cats'

    # def get_queryset(self):
    #     return Category.objects.filter(is_published=True)


# def index(request):
#     people =People.objects.all()
#     cats = Category.objects.all()
#     context = {'people':people, 'cats':cats}
#     return render(request, 'people/index.html', context)

    
def our_way(request):
    return render(request, 'people/our_way.html')


def contacts(request):
    return render(request, 'people/contacts.html')


class AddPost(CreateView):
    form_class = PeopleForm
    template_name = 'people/addpost.html'
    success_url = reverse_lazy('index')

# def addpost(request):
#     if request.method == 'POST':
#         form = PeopleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = PeopleForm()

#     return render(request, 'people/addpost.html', {'form':form})


# class PeopleBusinessman(ListView):
#     model = People
#     template_name = 'people/businessman.html'
#     context_object_name = 'people'

#     def get_queryset(self):
#         return Category.objects.filter(id__id=self.kwargs['p_id'],is_published=True)


def businessman(request, p_id):
    people =People.objects.filter(cat_id=p_id)
    cats = Category.objects.all()
    context = {'people':people, 'cats':cats, 'test_id':p_id}
    return render(request, 'people/businessman.html', context)

# Create your views here.

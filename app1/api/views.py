from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.core.paginator import Paginator
from app1.models import MockupItem
from app1.api.serializers import MockupSerializer
import requests
from django.views.generic.list import ListView


# def mockupdatafun(request):
#     response_data = requests.get('https://fakestoreapi.com/products').json()
#     serializer = MockupSerializer(data = response_data)
#     page_number = request.GET.get('page')
#     paginator = Paginator(serializer.initial_data, 8)
#     page_obj = paginator.get_page(page_number)
#     return render(request,"mockupdata.html", { "response_data":serializer.initial_data , "items" : page_obj})   

class MockupViewView(ListView):
    model = MockupItem
    paginate_by = 10
    template_name = "mockupdata.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response_data = requests.get('https://fakestoreapi.com/products').json()
        serializer = MockupSerializer(data = response_data)
        context['items_list'] = serializer.initial_data
        return context



@api_view(['GET', ])
def mocksingleproductfun(request,slug):
    item = get_object_or_404(MockupItem, slug=slug)

    context = {
        "item" : item,
    }
    return render(request,"mockupdetail.html",context)


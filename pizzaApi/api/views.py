from django.shortcuts import render
from rest_framework import generics
from .serializers import PizzaSerializer
from .models import Pizza
# Create your views here.

class PizzaCreateView(generics.CreateAPIView):
    lookup_field = 'id'
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class PizzaListView(generics.ListAPIView):
    lookup_field = 'id'
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filterset_fields = ['type','size']
    
class PizzaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    
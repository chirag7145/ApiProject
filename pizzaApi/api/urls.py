from django.urls import path
from .views import PizzaListView,PizzaCreateView,PizzaRetrieveUpdateDestroyView

urlpatterns = [
    path('pizzas/',PizzaListView.as_view(),name='pizza-list'),
    path('pizza/create/',PizzaCreateView.as_view(),name='pizza-create'),
    path('pizza/<int:id>/',PizzaRetrieveUpdateDestroyView.as_view(),name='pizza'),
]

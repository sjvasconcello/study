
from django.urls import path
from .views import MyOderView, CreateOrderProductView

urlpatterns = [
    path('mi-orden/', MyOderView.as_view(), name='my_order'),
    path('agregar-producto',CreateOrderProductView.as_view(), name="add_product")
]

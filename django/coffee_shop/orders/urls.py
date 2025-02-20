
from django.urls import path
from .views import MyOderView

urlpatterns = [
    path('mi-orden/', MyOderView.as_view(), name='my_order')
]

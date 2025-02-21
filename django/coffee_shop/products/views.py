
from django.urls import reverse_lazy
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import ProductForm
from .models import Product
from .serializers import ProductSerializer

class ProductFormView(generic.FormView):
    template_name = "products/add_products.html"
    form_class = ProductForm
    success_url = reverse_lazy('add_products')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/list_products.html'
    context_object_name = 'products'

# Django rest framework
class ProductListAPI(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
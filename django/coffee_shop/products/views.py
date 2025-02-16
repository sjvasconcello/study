
from django.urls import reverse_lazy
from django.views import generic
from .forms import ProductForm
from .models import Product

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


from django.urls import reverse_lazy
from django.views import generic
from .forms import ProductForm
# Create your views here.


class ProductFormView(generic.FormView):
    template_name = "products/add_products.html"
    form_class = ProductForm
    success_url = reverse_lazy('add_products')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
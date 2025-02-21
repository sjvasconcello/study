from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

class LogoutView(BaseLogoutView):
    """
    Vista para cerrar sesión, eliminar la sesión y redirigir a la lista de productos.
    """
    next_page = reverse_lazy('list_product')

    def dispatch(self, request, *args, **kwargs):
        request.session.flush()  # Eliminar la sesión completamente
        return super().dispatch(request, *args, **kwargs)

from django.views.generic import ListView
from section3.pregunta1.modelo import Producto


class VistaDeProductos(ListView):
    model = Producto
    template_name = 'lista_productos.html'
    context_object_name = 'productos'
    paginate_by = 10

from django.views.generic.base import TemplateView
from .models import Dog

class Home(TemplateView):
    template_name = 'home.html'
    
class About(TemplateView):
    template_name = 'about.html'

class DogList(TemplateView):
    template_name = 'dog_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dogs'] = Dog.objects.all()
        return context

# Create your views here.

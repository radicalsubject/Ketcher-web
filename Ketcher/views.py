from django.shortcuts import render
from django.views.generic import TemplateView

class KetcherTemplate(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)

def home(request):
    return render(request, 'index.html')

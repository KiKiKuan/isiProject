from django.shortcuts import render
from django.views.generic import TemplateView
#from .models import isiapp
class HomePageView(TemplateView):
    
    template_name='home.html'

# Create your views here.

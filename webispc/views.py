from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DateDetailView
from django.views.generic import ListView, DetailView, TemplateView, View
#from webispc.models import  
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django_xhtml2pdf.views import PdfMixin
from django_xhtml2pdf.utils import pdf_decorator
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.core.paginator import Paginator



def home(request):
    return render(request,'index.html')


class About(TemplateView):
    template_name = "about.html"


class Contacto(TemplateView):
    template_name = "contacto.html"
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib import admin
from webispc.views import home, Contacto, About


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',home, name="index"),  
    path('contacto/', Contacto.as_view(), name="contacto"),
    path('about/', About.as_view(), name="about"),

]
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, UpdateView
from accounts.forms import MyUserCreationForm, MyUserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.models import MasDatosUsuario
from django.conf import settings
from django.http import HttpResponse, JsonResponse
import smtplib
from django.contrib import messages #mensajes flotantes


class PanelLogin(LoginView):
    template_name = 'accounts/panel_login.html'
    next_page = reverse_lazy("index")


class PanelLogout(LogoutView):
    template_name = 'accounts/panel_logout.html'


class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'accounts/panel_signup.html'
  success_url = reverse_lazy('panel-login')
  form_class = MyUserCreationForm
  success_message = "¡Tu perfil Se creo satisfactoriamente !!"


@login_required
def perfil(request):
    return render(request, 'accounts/perfil.html')

@login_required
def editar_perfil(request):
    user = request.user
    mas_datos_usuario, _ = MasDatosUsuario.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = MyUserEditForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('first_name'):
                user.first_name = data.get('first_name')
            if data.get('last_name'):
                user.last_name = data.get('last_name')
            if data.get('email'):
                user.email = data.get('email')
            mas_datos_usuario.avatar = data.get('avatar') if data.get('avatar') else mas_datos_usuario.avatar  #seria otra forma de corroborar
            if data.get('password1') and data.get('password1') == data.get('password2'): # Permitimos asi el cambio de contraseña corroborando 
                user.set_password = data.get(password1)                                  # que no estan vacios y que sean iguales
            mas_datos_usuario.save()  #guardamos lo relacionado al usuario
            user.save() #guardamos al usuario
            messages.success(request, "Editado correctamente") #mensajes flotantes
            return redirect('perfil')
        else:
            return render(request, 'accounts/editar_perfil.html', {'form':form})
    
    form = MyUserEditForm(



        initial= {

            'email': user.email,
            'first_name' : user.first_name,
            'last_name' : user.last_name,
            'avatar' : mas_datos_usuario.avatar
        }
    )

    return render(request, 'accounts/editar_perfil.html',{'form':form})
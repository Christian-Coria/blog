from django.urls import path
from.views import PanelLogin, PanelLogout, SignUpView
from accounts.views import perfil , editar_perfil



urlpatterns = [
    
    path("login/", PanelLogin.as_view(), name="panel-login"),
    path("logout/", PanelLogout.as_view(), name="panel-logout"),
    path("signup/", SignUpView.as_view(), name="panel-signup"),
    path("perfil/", perfil, name="perfil"),
    path("editar/perfil/", editar_perfil, name="editar_perfil"),

]
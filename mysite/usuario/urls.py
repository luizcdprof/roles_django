from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.usuario_cadastrar_view, name='usuario_cadastrar'),
    path('listar/', views.usuario_listar_view, name='usuario_listar'),
    path('login/', views.usuario_login_view, name='usuario_login'),
    path('painel/', views.usuario_painel_view, name='usuario_painel'),
    path('sair/', views.usuario_logout_view, name='usuario_sair'),
]
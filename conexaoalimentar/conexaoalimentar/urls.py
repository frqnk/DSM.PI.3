
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('pagina_sucesso/', views.pagina_sucesso, name='sucesso'),
    path('listar/', views.listar_doacoes, name='listar'),
    path('editar_doacao/<str:doacao_id>/', views.editar_doacao, name='editar_doacao'),
    path('excluir_doacao/<str:doacao_id>/', views.excluir_doacao, name='excluir_doacao'),
]

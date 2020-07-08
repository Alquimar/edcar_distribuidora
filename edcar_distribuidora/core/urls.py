from django.urls import path

from edcar_distribuidora.core import views

app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
    path("quem-somos/", views.quem_somos, name="quem_somos"),
    path("contato/", views.contato, name="contato"),
    path("categoria/<int:categoria_id>", views.itens_categoria, name="itens_categoria"),
]
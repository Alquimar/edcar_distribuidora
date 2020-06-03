from django.urls import path

from edcar_distribuidora.core import views

app_name = "core"
urlpatterns = [
    path("", views.getTodos, name="home"),
    path("categoria/<int:categoria_id>", views.getItensCategoria, name="itens_categoria"),
]
from django.urls import path

from . import views

app_name = "estoque"

urlpatterns = [
    path("", views.produto_listar, name="produto_listar"),
    path("produtos/novo/", views.produto_criar, name="produto_criar"),
    path(
        "produtos/<int:pk>/editar/",
        views.produto_editar,
        name="produto_editar",
    ),
    path(
        "produtos/<int:pk>/excluir/",
        views.produto_excluir,
        name="produto_excluir",
    ),
]
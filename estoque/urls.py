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
    path(
        "entradas/",
        views.entrada_listar,
        name="entrada_listar",
    ),
    path(
        "entradas/nova/",
        views.entrada_criar,
        name="entrada_criar",
    ),
]
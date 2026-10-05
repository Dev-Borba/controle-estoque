from django.contrib import messages
from django.core.paginator import Paginator
from django.db import IntegrityError, transaction
from django.db.models import Q
from django.db.models.deletion import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET, require_http_methods

from .forms import ProdutoForm
from .models import Produto


@require_GET
def produto_listar(request):
    busca = request.GET.get("q", "").strip()[:100]
    produtos = Produto.objects.all()

    if busca:
        produtos = produtos.filter(
            Q(nome__icontains=busca)
            | Q(codigo__icontains=busca)
            | Q(categoria__icontains=busca)
        )

    total_resultados = produtos.count()
    pagina = Paginator(produtos, 15).get_page(request.GET.get("page"))

    return render(request, "estoque/produto_listar.html", {
        "pagina": pagina,
        "busca": busca,
        "total_resultados": total_resultados,
        "total_produtos": Produto.objects.count(),
    })


def _salvar_produto(request, produto=None):
    """Fluxo usado pelo cadastro e pela edição."""
    criando = produto is None

    form = ProdutoForm(
        request.POST if request.method == "POST" else None,
        instance=produto,
    )

    if request.method == "POST" and form.is_valid():
        try:
            with transaction.atomic():
                form.save()
        except IntegrityError:
            form.add_error("codigo", "Já existe um produto com este código.")
        else:
            messages.success(
                request,
                "Produto cadastrado com sucesso." if criando
                else "Produto atualizado com sucesso.",
            )
            return redirect("estoque:produto_listar")

    return render(request, "estoque/produto_form.html", {
        "form": form,
        "titulo": "Novo produto" if criando else "Editar produto",
        "criando": criando,
        "produto": produto,
    })


@require_http_methods(["GET", "POST"])
def produto_criar(request):
    return _salvar_produto(request)


@require_http_methods(["GET", "POST"])
def produto_editar(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return _salvar_produto(request, produto)


@require_http_methods(["GET", "POST"])
def produto_excluir(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == "POST":
        if produto.saldo:
            messages.error(
                request,
                "Este produto possui saldo e não pode ser excluído.",
            )
        else:
            try:
                produto.delete()
            except ProtectedError:
                messages.error(
                    request,
                    "Este produto possui registros vinculados e não pode ser excluído.",
                )
            else:
                messages.success(request, "Produto excluído com sucesso.")

        return redirect("estoque:produto_listar")

    return render(request, "estoque/produto_excluir.html", {
        "produto": produto,
        "pode_excluir": produto.saldo == 0,
    })
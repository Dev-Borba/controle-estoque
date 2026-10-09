import csv
from urllib.parse import urlencode

from django.contrib import messages
from django.core.paginator import Paginator
from django.db import IntegrityError, transaction
from django.db.models import BooleanField, Case, F, Q, Value, When
from django.db.models.deletion import ProtectedError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET, require_http_methods

from .forms import EntradaEstoqueForm, ProdutoForm, SaidaEstoqueForm
from .models import EntradaEstoque, Produto, SaidaEstoque


# --------------------------------------------------
# AC1 — Produtos
# --------------------------------------------------

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
    pagina = Paginator(produtos, 15).get_page(
        request.GET.get("page"),
    )

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
            form.add_error(
                "codigo",
                "Já existe um produto com este código.",
            )
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
                    "Este produto possui registros vinculados "
                    "e não pode ser excluído.",
                )
            else:
                messages.success(
                    request,
                    "Produto excluído com sucesso.",
                )

        return redirect("estoque:produto_listar")

    return render(request, "estoque/produto_excluir.html", {
        "produto": produto,
        "pode_excluir": produto.saldo == 0,
    })


# --------------------------------------------------
# AC2 — Entradas de estoque
# --------------------------------------------------

@require_http_methods(["GET", "POST"])
def entrada_criar(request):
    form = EntradaEstoqueForm(
        request.POST if request.method == "POST" else None,
    )

    if request.method == "POST" and form.is_valid():
        produto_id = form.cleaned_data["produto"].pk
        quantidade = form.cleaned_data["quantidade"]
        entrada_salva = False

        try:
            with transaction.atomic():
                produto = (
                    Produto.objects
                    .select_for_update()
                    .get(pk=produto_id)
                )

                novo_saldo = produto.saldo + quantidade

                if novo_saldo > 2147483647:
                    form.add_error(
                        "quantidade",
                        "Esta quantidade ultrapassa o limite do saldo.",
                    )
                else:
                    entrada = form.save(commit=False)
                    entrada.produto = produto
                    entrada.save()

                    produto.saldo = novo_saldo
                    produto.save(
                        update_fields=["saldo", "atualizado_em"],
                    )

                    entrada_salva = True

        except Produto.DoesNotExist:
            form.add_error(
                "produto",
                "Este produto foi excluído. Selecione outro produto.",
            )
        except IntegrityError:
            form.add_error(
                None,
                "Não foi possível registrar a entrada. "
                "Confira os dados e tente novamente.",
            )

        if entrada_salva:
            messages.success(
                request,
                f"Entrada de {quantidade} registrada para "
                f"{produto.codigo}. Saldo atual: {novo_saldo}.",
            )
            return redirect("estoque:entrada_listar")

    return render(request, "estoque/entrada_form.html", {
        "form": form,
        "titulo": "Nova entrada de estoque",
    })


@require_GET
def entrada_listar(request):
    busca = request.GET.get("q", "").strip()[:100]

    entradas = EntradaEstoque.objects.select_related("produto")

    if busca:
        entradas = entradas.filter(
            Q(produto__codigo__icontains=busca)
            | Q(produto__nome__icontains=busca)
            | Q(observacao__icontains=busca)
        )

    total_resultados = entradas.count()
    pagina = Paginator(entradas, 15).get_page(
        request.GET.get("page"),
    )

    return render(request, "estoque/entrada_listar.html", {
        "pagina": pagina,
        "busca": busca,
        "total_resultados": total_resultados,
        "total_entradas": EntradaEstoque.objects.count(),
    })


# --------------------------------------------------
# AC3 — Saídas de estoque
# --------------------------------------------------

@require_http_methods(["GET", "POST"])
def saida_criar(request):
    form = SaidaEstoqueForm(
        request.POST if request.method == "POST" else None,
    )

    if request.method == "POST" and form.is_valid():
        produto_id = form.cleaned_data["produto"].pk
        quantidade = form.cleaned_data["quantidade"]
        saida_salva = False

        try:
            with transaction.atomic():
                produto = (
                    Produto.objects
                    .select_for_update()
                    .get(pk=produto_id)
                )

                if quantidade > produto.saldo:
                    form.add_error(
                        "quantidade",
                        f"Estoque insuficiente. "
                        f"Saldo disponível: {produto.saldo}.",
                    )
                else:
                    novo_saldo = produto.saldo - quantidade

                    saida = form.save(commit=False)
                    saida.produto = produto
                    saida.save()

                    produto.saldo = novo_saldo
                    produto.save(
                        update_fields=["saldo", "atualizado_em"],
                    )

                    saida_salva = True

        except Produto.DoesNotExist:
            form.add_error(
                "produto",
                "Este produto foi excluído. Selecione outro produto.",
            )
        except IntegrityError:
            form.add_error(
                None,
                "Não foi possível registrar a saída. "
                "Confira os dados e tente novamente.",
            )

        if saida_salva:
            messages.success(
                request,
                f"Saída de {quantidade} registrada para "
                f"{produto.codigo}. Saldo atual: {novo_saldo}.",
            )
            return redirect("estoque:saida_listar")

    return render(request, "estoque/saida_form.html", {
        "form": form,
        "titulo": "Nova saída de estoque",
    })


@require_GET
def saida_listar(request):
    busca = request.GET.get("q", "").strip()[:100]

    saidas = SaidaEstoque.objects.select_related("produto")

    if busca:
        saidas = saidas.filter(
            Q(produto__codigo__icontains=busca)
            | Q(produto__nome__icontains=busca)
            | Q(observacao__icontains=busca)
        )

    total_resultados = saidas.count()
    pagina = Paginator(saidas, 15).get_page(
        request.GET.get("page"),
    )

    return render(request, "estoque/saida_listar.html", {
        "pagina": pagina,
        "busca": busca,
        "total_resultados": total_resultados,
        "total_saidas": SaidaEstoque.objects.count(),
    })


# --------------------------------------------------
# PROVA — Relatório de estoque
# --------------------------------------------------

def _filtrar_relatorio(request):
    """Aplica os mesmos filtros à tela e à exportação CSV."""
    busca = request.GET.get("q", "").strip()[:100]
    categoria = request.GET.get("categoria", "").strip()[:100]
    somente_baixo = request.GET.get("estoque_baixo") == "1"

    produtos = Produto.objects.annotate(
        estoque_baixo=Case(
            When(
                saldo__lte=F("estoque_minimo"),
                then=Value(True),
            ),
            default=Value(False),
            output_field=BooleanField(),
        ),
    )

    if busca:
        produtos = produtos.filter(
            Q(nome__icontains=busca)
            | Q(codigo__icontains=busca)
        )

    if categoria:
        produtos = produtos.filter(
            categoria=categoria,
        )

    if somente_baixo:
        produtos = produtos.filter(
            saldo__lte=F("estoque_minimo"),
        )

    produtos = produtos.order_by("nome", "pk")

    return produtos, busca, categoria, somente_baixo


@require_GET
def relatorio_estoque(request):
    produtos, busca, categoria, somente_baixo = (
        _filtrar_relatorio(request)
    )

    total_resultados = produtos.count()

    total_estoque_baixo = produtos.filter(
        saldo__lte=F("estoque_minimo"),
    ).count()

    pagina = Paginator(produtos, 15).get_page(
        request.GET.get("page"),
    )

    categorias = (
        Produto.objects
        .exclude(categoria="")
        .order_by("categoria")
        .values_list("categoria", flat=True)
        .distinct()
    )

    parametros = {
        "q": busca,
        "categoria": categoria,
    }

    if somente_baixo:
        parametros["estoque_baixo"] = "1"

    filtros_query = urlencode(parametros)

    return render(request, "estoque/relatorio_estoque.html", {
        "pagina": pagina,
        "busca": busca,
        "categoria": categoria,
        "categorias": categorias,
        "somente_baixo": somente_baixo,
        "total_resultados": total_resultados,
        "total_estoque_baixo": total_estoque_baixo,
        "filtros_query": filtros_query,
    })


def _texto_seguro_csv(valor):
    """Evita interpretar textos cadastrados como fórmulas."""
    texto = str(valor)

    if texto.lstrip().startswith(("=", "+", "-", "@")):
        return "'" + texto

    if texto.startswith(("\t", "\r", "\n")):
        return "'" + texto

    return texto


@require_GET
def relatorio_exportar_csv(request):
    produtos, _, _, _ = _filtrar_relatorio(request)

    resposta = HttpResponse(
        content_type="text/csv; charset=utf-8",
    )
    resposta["Content-Disposition"] = (
        'attachment; filename="relatorio_estoque.csv"'
    )
    resposta["Cache-Control"] = "no-store"

    # Facilita o reconhecimento dos acentos pelo Excel.
    resposta.write("\ufeff")

    escritor = csv.writer(
        resposta,
        delimiter=";",
        lineterminator="\r\n",
    )

    escritor.writerow([
        "Código",
        "Nome",
        "Categoria",
        "Unidade",
        "Saldo atual",
        "Estoque mínimo",
        "Situação do estoque",
    ])

    # Exporta todos os resultados filtrados, sem paginação.
    for produto in produtos.iterator(chunk_size=1000):
        escritor.writerow([
            _texto_seguro_csv(produto.codigo),
            _texto_seguro_csv(produto.nome),
            _texto_seguro_csv(produto.categoria),
            _texto_seguro_csv(produto.get_unidade_display()),
            produto.saldo,
            produto.estoque_minimo,
            "Estoque baixo" if produto.estoque_baixo
            else "Acima do mínimo",
        ])

    return resposta
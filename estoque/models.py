from decimal import Decimal

from django.core.validators import MinValueValidator, RegexValidator
from django.db import models
from django.db.models.functions import Upper


class Produto(models.Model):
    class Unidade(models.TextChoices):
        UNIDADE = "UN", "Unidade"
        PECA = "PC", "Peça"
        CAIXA = "CX", "Caixa"

    codigo = models.CharField(
        "Código / SKU",
        max_length=40,
        unique=True,
        validators=[
            RegexValidator(
                r"^[A-Za-z0-9][A-Za-z0-9._-]*$",
                "Use letras, números, ponto, hífen ou sublinhado, sem espaços.",
            )
        ],
        help_text="Identificador único do produto. Exemplo: TEC-001.",
        error_messages={"unique": "Já existe um produto com este código."},
    )
    nome = models.CharField("Nome do produto", max_length=150)
    categoria = models.CharField(
        "Categoria", max_length=100, blank=True,
        help_text="Opcional. Exemplo: Periféricos.",
    )
    unidade = models.CharField(
        "Unidade de contagem", max_length=2,
        choices=Unidade.choices, default=Unidade.UNIDADE,
    )
    preco = models.DecimalField(
        "Preço de referência (R$)",
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00"),
        validators=[MinValueValidator(Decimal("0.00"))],
        help_text="Use vírgula para os centavos. Exemplo: 125,90.",
    )
    estoque_minimo = models.PositiveIntegerField(
        "Estoque mínimo", default=0,
        help_text="Quantidade inteira maior ou igual a zero.",
    )
    saldo = models.PositiveIntegerField(
        "Saldo atual", default=0, editable=False,
    )
    criado_em = models.DateTimeField("Cadastrado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        ordering = ["nome", "pk"]
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        constraints = [
            models.UniqueConstraint(
                Upper("codigo"),
                name="estoque_codigo_sem_diferenca_de_caixa",
                violation_error_message="Já existe um produto com este código.",
            ),
            models.CheckConstraint(
                condition=models.Q(preco__gte=0),
                name="estoque_preco_nao_negativo",
            ),
        ]

    def clean(self):
        super().clean()
        self.codigo = self.codigo.strip().upper()
        self.nome = self.nome.strip()
        self.categoria = self.categoria.strip()

    def save(self, *args, **kwargs):
        self.codigo = self.codigo.strip().upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo} — {self.nome}"
class EntradaEstoque(models.Model):
    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT,
        related_name="entradas",
        verbose_name="Produto",
    )
    quantidade = models.PositiveIntegerField(
        "Quantidade recebida",
        validators=[MinValueValidator(1)],
        help_text="Informe uma quantidade inteira maior que zero.",
    )
    observacao = models.CharField(
        "Observação",
        max_length=255,
        blank=True,
        help_text="Opcional. Exemplo: Compra de mercadoria.",
    )
    criado_em = models.DateTimeField(
        "Registrado em",
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-criado_em", "-pk"]
        verbose_name = "Entrada de estoque"
        verbose_name_plural = "Entradas de estoque"
        constraints = [
            models.CheckConstraint(
                condition=models.Q(quantidade__gte=1),
                name="estoque_entrada_quantidade_positiva",
            ),
        ]

    def clean(self):
        super().clean()
        self.observacao = self.observacao.strip()

    def __str__(self):
        return f"{self.produto.codigo} — Entrada de {self.quantidade}"

class SaidaEstoque(models.Model):
    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT,
        related_name="saidas",
        verbose_name="Produto",
    )
    quantidade = models.PositiveIntegerField(
        "Quantidade retirada",
        validators=[MinValueValidator(1)],
        help_text="Informe uma quantidade inteira maior que zero.",
    )
    observacao = models.CharField(
        "Observação",
        max_length=255,
        blank=True,
        help_text="Opcional. Exemplo: Venda de mercadoria.",
    )
    criado_em = models.DateTimeField(
        "Registrado em",
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-criado_em", "-pk"]
        verbose_name = "Saída de estoque"
        verbose_name_plural = "Saídas de estoque"
        constraints = [
            models.CheckConstraint(
                condition=models.Q(quantidade__gte=1),
                name="estoque_saida_quantidade_positiva",
            ),
        ]

    def clean(self):
        super().clean()
        self.observacao = self.observacao.strip()

    def __str__(self):
        return f"{self.produto.codigo} — Saída de {self.quantidade}"
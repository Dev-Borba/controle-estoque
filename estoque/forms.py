from django import forms

from .models import EntradaEstoque, Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            "codigo", "nome", "categoria", "unidade", "preco", "estoque_minimo",
        ]
        widgets = {
            "codigo": forms.TextInput(attrs={"placeholder": "TEC-001"}),
            "nome": forms.TextInput(attrs={"placeholder": "Teclado USB"}),
            "categoria": forms.TextInput(attrs={"placeholder": "Periféricos"}),
            "preco": forms.TextInput(
                attrs={"inputmode": "decimal", "placeholder": "0,00"},
            ),
            "estoque_minimo": forms.NumberInput(
                attrs={"min": "0", "step": "1"},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["preco"].localize = True
        self.fields["preco"].widget.is_localized = True

        for name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["aria-describedby"] = (
                f"id_{name}_help id_{name}_errors"
            )

    def clean_codigo(self):
        return self.cleaned_data["codigo"].strip().upper()


class EntradaEstoqueForm(forms.ModelForm):
    class Meta:
        model = EntradaEstoque
        fields = ["produto", "quantidade", "observacao"]
        widgets = {
            "produto": forms.Select(),
            "quantidade": forms.NumberInput(
                attrs={"min": "1", "step": "1", "placeholder": "Exemplo: 10"},
            ),
            "observacao": forms.TextInput(
                attrs={"placeholder": "Exemplo: Compra de mercadoria"},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["produto"].empty_label = "Selecione um produto"

        for name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["aria-describedby"] = (
                f"id_{name}_help id_{name}_errors"
            )

    def clean_quantidade(self):
        quantidade = self.cleaned_data["quantidade"]

        if quantidade <= 0:
            raise forms.ValidationError(
                "Informe uma quantidade maior que zero."
            )

        return quantidade

    def clean_observacao(self):
        return self.cleaned_data.get("observacao", "").strip()
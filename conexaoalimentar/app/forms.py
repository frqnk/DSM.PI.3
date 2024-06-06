from django import forms
from .models import Doacao


class ProdutoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    quantidade = forms.IntegerField(min_value=1)


class DoacaoForm(forms.ModelForm):
    local_destino = forms.ChoiceField(choices=[('local1', 'Local 1'), ('local2', 'Local 2'), ('local3', 'Local 3')],
                                      required=False, label='Local de Destino', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Doacao
        # Inclua outros campos do modelo aqui, se houver
        fields = ['nome', 'documento']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.produtos_forms = [ProdutoForm(prefix=str(
            i)) for i in range(5)]  # Permitir 5 produtos

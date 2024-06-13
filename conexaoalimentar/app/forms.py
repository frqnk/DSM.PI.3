from django import forms
from .models import Doacao


class ProdutoForm(forms.Form):
    nome = forms.CharField(max_length=100, required=False)
    quantidade = forms.IntegerField(min_value=1, required=False)


class DoacaoForm(forms.ModelForm):
    local_destino = forms.ChoiceField(choices=[('local1', 'Amparaí '),
                                               ('local2', 'Amigos do Bem'),
                                               ('local3', 'Banco de Alimentos - ABNE'),
                                               ('local4',
                                                'Cozinha - Tem Gente com Fome'),
                                               ('local5', 'ActionAid')],
                                      required=False, label='Local de Destino', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Doacao
        # Inclua outros campos do modelo aqui, se houver
        fields = ['nome', 'documento']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.produtos_forms = [ProdutoForm(prefix=str(
            i)) for i in range(5)]  # Permitir 5 produtos

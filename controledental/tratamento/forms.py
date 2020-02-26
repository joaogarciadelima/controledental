from django.forms import ModelForm, NumberInput, Textarea

from controledental.tratamento.models import CadastroTratamento
from controledental.pacientes.models import Paciente


class TratamentoForm(ModelForm):
    class Meta:
        model = CadastroTratamento
        fields = ['nome_tratamento', 'valor_tratamento']
        widgets = {
            'observacao': Textarea(attrs={'class': 'form-control'}),
        }


class PacienteTratamento(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome']
        widgets = {
            'quantidade': NumberInput(attrs={'class': 'form-control'}),
        }

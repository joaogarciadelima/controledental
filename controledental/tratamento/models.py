from django.db import models
from django.utils import timezone

from controledental.pacientes.models import Paciente
from controledental.cadastrotratamento.models import CadastroTratamento


class Tratamento(models.Model):
    class Meta:
        verbose_name = 'Tratamento'
        verbose_name_plural = 'Tratamentos'

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,)
    tratamento = models.ForeignKey(CadastroTratamento, on_delete=models.CASCADE, verbose_name='Tratamento',
                                   default=None,)
    DENTE = [

        ("0-TODOS", "TODOS"),
        ("11-INCISIVO CENTRAL SUPERIOR", "11-INCISIVO CENTRAL SUPERIOR"),
        ("21-INCISIVO CENTRAL SUPERIOR", "21-INCISIVO CENTRAL SUPERIOR"),
        ("12-INCISIVO LATERAL SUPERIOR", "12-INCISIVO LATERAL SUPERIOR"),
        ("22-INCISIVO LATERAL SUPERIOR", "22-INCISIVO LATERAL SUPERIOR"),
        ("13-CANINO SUPERIOR", "13-CANINO SUPERIOR"),
        ("23-CANINO SUPERIOR", "23-CANINO SUPERIOR"),
        ("14-PRE-MOLAR SUPERIOR", "14-PRE-MOLAR SUPERIOR"),
        ("15-PRE-MOLAR SUPERIOR", "15-PRE-MOLAR SUPERIOR"),
        ("24-PRE-MOLAR SUPERIOR", "24-PRE-MOLAR SUPERIOR"),
        ("25-PRE-MOLAR SUPERIOR", "25-PRE-MOLAR SUPERIOR"),
        ("16-MOLAR SUPERIOR", "16-MOLAR SUPERIOR"),
        ("17-MOLAR SUPERIOR", "17-MOLAR SUPERIOR"),
        ("18-MOLAR SUPERIOR", "18-MOLAR SUPERIOR"),
        ("26-MOLAR SUPERIOR", "26-MOLAR SUPERIOR"),
        ("27-MOLAR SUPERIOR", "27-MOLAR SUPERIOR"),
        ("28-MOLAR SUPERIOR", "28-MOLAR SUPERIOR"),
        ("31-INCISIVO CENTRAL INFERIOR", "31-INCISIVO CENTRAL INFERIOR"),
        ("41-INCISIVO CENTRAL INFERIOR", "41-INCISIVO CENTRAL INFERIOR"),
        ("32-INCISIVO LATERAL INFERIOR", "32-INCISIVO LATERAL INFERIOR"),
        ("42-INCISIVO LATERAL INFERIOR", "42-INCISIVO LATERAL INFERIOR"),
        ("33-CANINO INFERIOR", "33-CANINO INFERIOR"),
        ("43-CANINO INFERIOR", "43-CANINO INFERIOR"),
        ("34-PRE MOLAR INFERIOR", "34-PRE MOLAR INFERIOR"),
        ("35-PRE MOLAR INFERIOR", "35-PRE MOLAR INFERIOR"),
        ("44-PRE MOLAR INFERIOR", "44-PRE MOLAR INFERIOR"),
        ("45-PRE MOLAR INFERIOR", "45-PRE MOLAR INFERIOR"),
        ("36-MOLAR INFERIOR", "36-MOLAR INFERIOR"),
        ("37-MOLAR INFERIOR", "37-MOLAR INFERIOR"),
        ("38-MOLAR INFERIOR", "38-MOLAR INFERIOR"),
        ("46-MOLAR INFERIOR", "46-MOLAR INFERIOR"),
        ("47-MOLAR INFERIOR", "47-MOLAR INFERIOR"),
        ("48-MOLAR INFERIOR", "48-MOLAR INFERIOR"),
    ]
    dente = models.CharField(max_length=60, choices=DENTE, verbose_name='Dente')
    observacao = models.CharField(max_length=5000, verbose_name="Observação")
    valor_tratamento = models.DecimalField(decimal_places=2, max_digits=8, verbose_name='valor', null=False, default=0)
    data_tratamento = models.DateField(verbose_name="Data Tratamento", default=timezone.now)

    def __repr__(self):
        return f'paciente{self.paciente},tratamento{self.tratamento}, datatratamento{self.data_tratamento}' \
               f', observacao={self.observacao!r}'

from django.contrib import admin
from controledental.tratamento.models import Tratamento


@admin.register(Tratamento)
class TratamentoAdmin(admin.ModelAdmin):
    list_display = 'paciente tratamento dente observacao'.split()
    ordering = ('tratamento',)

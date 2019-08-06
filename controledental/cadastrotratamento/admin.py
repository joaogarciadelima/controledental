from django.contrib import admin
from controledental.cadastrotratamento.models import CadastroTratamento


@admin.register(CadastroTratamento)
class CadastroTratamentoAdmin(admin.ModelAdmin):
    list_display = 'nome_tratamento observacao'.split()
    ordering = ('nome_tratamento',)

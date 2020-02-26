from django.contrib import admin
from controledental.tratamento.models import Tratamento


@admin.register(Tratamento)
class TratamentoAdmin(admin.ModelAdmin):
    list_display = 'paciente tratamento data_tratamento dente observacao valor_tratamento'.split()
    ordering = ('tratamento',)
#
# class MatriculaInline(admin.TabularInline):
#     model = Turma.alunos.through
#     extra = 1
#     readonly_fields = ('data',)
#     autocomplete_fields = ('usuario',)
#     ordering = ('-data',)
#
#
# @admin.register(Turma)
# class TurmaAdmin(admin.ModelAdmin):
#     inlines = [MatriculaInline]
#     list_display = ('nome', 'slug', 'inicio', 'fim')
#     prepopulated_fields = {'slug': ('nome',)}
#     ordering = ('-inicio',)

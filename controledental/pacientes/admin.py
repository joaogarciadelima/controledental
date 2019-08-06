from django.contrib import admin
from controledental.pacientes.models import Paciente


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = 'nome telefone email'.split()
    ordering = ('nome',)

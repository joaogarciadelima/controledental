from django.shortcuts import render

from controledental.pacientes.models import Paciente


def pacientes(request):
    query_set = Paciente.objects.order_by('nome')
    ctx = {
        'Pacientes': list(query_set)
    }
    return render(request, 'pacientes/pacientes.html', context=ctx)

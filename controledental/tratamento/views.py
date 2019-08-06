# from django.shortcuts import render
#
# from controledental.tratamento.models import Tratamento
#
#
# def tratamentos(request):
#     query_set = Tratamento.objects.order_by('nome')
#     ctx = {
#         'Tratamentos': list(query_set)
#     }
#     return render(request, 'tratamento/tratamento.html', context=ctx)

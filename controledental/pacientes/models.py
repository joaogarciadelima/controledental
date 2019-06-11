from django.db import models


class Paciente(models.Model):
    nome = models.CharField(max_length=80)
    data_nascimento = models.DateField()
    rg = models.CharField(max_length=25)
    cpf = models.CharField(max_length=25)
    endereco = models.CharField(verbose_name='Endereço', max_length=50)
    telefone = models.CharField(verbose_name='Telefone', max_length=25)
    observacao = models.CharField(verbose_name='Observações', max_length=2000)
    alergia = models.CharField(verbose_name='Alergias', max_length=100)
    medicamentos = models.CharField(verbose_name='Medicamentos', max_length=500)
    historico_cirurgias = models.CharField(verbose_name='Cirurgias', max_length=2000)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return f'nome={self.nome!r}, endereco={self.endereco!r}, telefone={self.telefone!r}'

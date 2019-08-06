from django.db import models


class Paciente(models.Model):
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
    nome = models.CharField(max_length=80)
    data_nascimento = models.DateField()
    rg = models.CharField(max_length=25)
    cpf = models.CharField(max_length=25)
    endereco = models.CharField(verbose_name='Endereço', max_length=50)
    telefone = models.CharField(verbose_name='Telefone', max_length=25)
    alergia = models.CharField(verbose_name='Alergias', max_length=100)
    medicamentos = models.CharField(verbose_name='Medicamentos', max_length=500)
    historico_cirurgias = models.CharField(verbose_name='Cirurgias', max_length=2000)
    observacao = models.CharField(verbose_name='Observações', max_length=2000)
    email = models.EmailField(verbose_name='Email', null=True, max_length=200)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return f'nome={self.nome!r}, endereco={self.endereco!r}, telefone={self.telefone!r}, email={self.email!r}'

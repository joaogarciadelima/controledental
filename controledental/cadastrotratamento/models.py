from django.db import models


class CadastroTratamento(models.Model):
    class Meta:
        verbose_name = 'Cadastro Tratamento'
        verbose_name_plural = 'Cadastro de tratamentos'

    nome_tratamento = models.CharField(max_length=200, verbose_name='Nome Tratamento')
    observacao = models.CharField(max_length=2000, verbose_name="Observações", default=None)

    def __str__(self):
        return self.nome_tratamento

    def __repr__(self):
        return f'nome_tratamento={self.nome_tratamento!r}, observacao={self.observacao!r}'

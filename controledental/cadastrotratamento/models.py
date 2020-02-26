from django.db import models


class CadastroTratamento(models.Model):
    class Meta:
        verbose_name = 'Cadastro Tratamento'
        verbose_name_plural = 'Cadastro de tratamentos'

    nome_tratamento = models.CharField(max_length=200, verbose_name='Nome Tratamento')
    valor_tratamento = models.DecimalField(decimal_places=2, max_digits=8, verbose_name='valor', null=False, default=0)
    observacao = models.CharField(max_length=2000, verbose_name="Observações", default=None)

    def __str__(self):
        return self.nome_tratamento

    def __repr__(self):
        return f'nome_tratamento={self.nome_tratamento!r}, observacao={self.observacao!r},' \
               f'valor={self.valor_tratamento!r}'

    def retorna_valor_tratamento(self):
        return self.valor_tratamento

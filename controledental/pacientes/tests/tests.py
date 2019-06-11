import pytest
from django.urls import reverse

from controledental.django_assertions import assert_contains
from controledental.pacientes.models import Paciente


@pytest.fixture
def pacientes(db):
    pacientes = Paciente(nome='João Garcia de Lima Neto',
                         data_nascimento='1982-11-12',
                         rg='mg11143198',
                         cpf='04887497601',
                         endereco='Av. Getulio Vargas, 830 apto 101',
                         telefone='037988323652',
                         observacao='nenhuma',
                         alergia='nenhuma',
                         medicamentos='nenhum',
                         historico_cirurgias='nenhuma'
                         )
    pacientes.save()
    return [pacientes]


@pytest.fixture
def resp(client, pacientes):
    resp = client.get(reverse('pacientes:pacientes'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Pacientes</title>')


def home_link(resp):
    assert_contains(resp, f'href="{reverse("pacientes:pacientes")}">Pacientes')

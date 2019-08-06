import pytest
from controledental.tratamento.models import Tratamento


@pytest.fixture
def tratamento(db):
    tratamentos = Tratamento(paciente=1,
                             tratamento=1,
                             dente="11-INCISIVO CENTRAL SUPERIOR",
                             observacao="Canal no incisivo central superior"
                             )
    tratamentos.save()
    return [tratamentos]


# def test_status_code(resp):
#     assert resp.status_code == 200

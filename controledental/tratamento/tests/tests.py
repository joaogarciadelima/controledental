import pytest
from model_mommy import mommy

from controledental.tratamento.models import Tratamento


@pytest.fixture
def tratamento(db):
    return mommy.make(Tratamento)


# def test_status_code(resp):
#     assert resp.status_code == 200

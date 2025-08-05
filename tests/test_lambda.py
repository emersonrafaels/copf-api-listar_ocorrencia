import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import pytest
from lambda_function import (resposta_ocorrencia_por_id, 
                             resposta_erro, 
                             resposta_sucesso)
from src.services import _OCORRENCIAS_MOCK


@pytest.mark.success
def test_resposta_ocorrencia_por_id_sucesso():
    # Testa busca de ocorrência existente
    ocorrencia_id = _OCORRENCIAS_MOCK[0].id
    path = f"/ocorrencias/{ocorrencia_id}"
    response = resposta_ocorrencia_por_id(path)
    assert response["statusCode"] == 200
    assert response["body"]
    assert str(ocorrencia_id) in response["body"]


@pytest.mark.error
def test_resposta_ocorrencia_por_id_nao_encontrada():
    # Testa busca de ocorrência inexistente
    path = "/ocorrencias/9999"
    response = resposta_ocorrencia_por_id(path)
    assert response["statusCode"] == 404
    assert "Ocorrência não encontrada" in response["body"]


@pytest.mark.edgecase
def test_resposta_ocorrencia_por_id_id_invalido():
    # Testa busca com ID inválido
    path = "/ocorrencias/abc"
    response = resposta_ocorrencia_por_id(path)
    assert response["statusCode"] == 400
    assert "ID inválido" in response["body"]

test_resposta_ocorrencia_por_id_sucesso()
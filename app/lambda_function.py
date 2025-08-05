import json
import sys
from pathlib import Path
from dataclasses import dataclass, asdict

sys.path.append(str(Path(__file__).resolve().parent))

from src.models import Ocorrencia
from src.services import listar_ocorrencias, buscar_ocorrencia_por_id

def resposta_raiz():
    """
    Retorna mensagem de boas-vindas da API.
    """
    return resposta_sucesso({"mensagem": "API Mock de Ocorrências Lambda"})

def resposta_listar_ocorrencias():
    """
    Retorna a lista de todas as ocorrências mockadas.
    """
    return resposta_sucesso([o.dict() for o in listar_ocorrencias()])

def resposta_ocorrencia_por_id(path: str):
    """
    Busca uma ocorrência pelo ID extraído da rota.
    Retorna a ocorrência se encontrada, erro caso contrário.
    """
    try:
        ocorrencia_id = int(path.rsplit("/", 1)[-1])
    except ValueError:
        return resposta_erro(400, "ID inválido")
    if (ocorrencia := buscar_ocorrencia_por_id(ocorrencia_id)):
        return resposta_sucesso(asdict(ocorrencia))
    return resposta_erro(404, "Ocorrência não encontrada")

def resposta_sucesso(body):
    """
    Retorna resposta de sucesso (HTTP 200) com o corpo fornecido.
    """
    return _response(200, body)

def resposta_erro(status_code: int, mensagem: str):
    """
    Retorna resposta de erro com o status e mensagem informados.
    """
    return _response(status_code, {"erro": mensagem})

def _response(status_code: int, body):
    """
    Monta o dicionário de resposta padrão da API Lambda.
    """
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body, ensure_ascii=False)
    }

def lambda_handler(event, context):
    """
    Handler principal da AWS Lambda para a API de ocorrências.
    Roteia requisições conforme path e método HTTP.
    """
    path = event.get("path", "")
    method = event.get("httpMethod", "GET")

    match (path, method):
        case ("/", "GET"):
            return resposta_raiz()
        case ("/ocorrencias", "GET"):
            return resposta_listar_ocorrencias()
        case (p, "GET") if p.startswith("/ocorrencias/"):
            return resposta_ocorrencia_por_id(p)
        case _:
            return resposta_erro(404, "Rota não encontrada")
import json
from dataclasses import dataclass, asdict
from typing import List
from datetime import date

@dataclass
class Ocorrencia:
    id: int
    data_ocorrencia: str  # ISO format: YYYY-MM-DD
    tipo: str
    descricao: str
    status: str

# 🔧 Mock de dados
ocorrencias_mock: List[Ocorrencia] = [
    Ocorrencia(1, "2025-08-01", "Alerta", "Sistema fora do ar", "aberto"),
    Ocorrencia(2, "2025-08-02", "Incidente", "Erro em login", "resolvido"),
    Ocorrencia(3, "2025-08-03", "Manutenção", "Atualização programada", "em andamento"),
]

def lambda_handler(event, context):
    path = event.get("path", "")
    method = event.get("httpMethod", "GET")

    if path == "/" and method == "GET":
        return _response(200, {"mensagem": "API Mock de Ocorrências Lambda"})

    elif path == "/ocorrencias" and method == "GET":
        return _response(200, [asdict(o) for o in ocorrencias_mock])

    elif path.startswith("/ocorrencias/") and method == "GET":
        try:
            ocorrencia_id = int(path.split("/")[-1])
            ocorrencia = next((o for o in ocorrencias_mock if o.id == ocorrencia_id), None)
            if ocorrencia:
                return _response(200, asdict(ocorrencia))
            else:
                return _response(404, {"erro": "Ocorrência não encontrada"})
        except ValueError:
            return _response(400, {"erro": "ID inválido"})

    return _response(404, {"erro": "Rota não encontrada"})

def _response(status_code: int, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }

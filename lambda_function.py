from fastapi import FastAPI
from dataclasses import dataclass, asdict
from typing import List
from datetime import date

app = FastAPI()

@dataclass
class Ocorrencia:
    id: int
    data_ocorrencia: date
    tipo: str
    descricao: str
    status: str

# 🧪 Mock de dados
ocorrencias_mock: List[Ocorrencia] = [
    Ocorrencia(1, date(2025, 8, 1), "Alerta", "Sistema fora do ar", "aberto"),
    Ocorrencia(2, date(2025, 8, 2), "Incidente", "Erro em login", "resolvido"),
    Ocorrencia(3, date(2025, 8, 3), "Manutenção", "Atualização programada", "em andamento"),
]

@app.get("/")
def home():
    return {"mensagem": "API Mock de Ocorrências"}

@app.get("/ocorrencias")
def listar_ocorrencias():
    return [asdict(o) for o in ocorrencias_mock]

@app.get("/ocorrencias/{id}")
def buscar_ocorrencia(id: int):
    ocorrencia = next((o for o in ocorrencias_mock if o.id == id), None)
    if not ocorrencia:
        return {"erro": "Ocorrência não encontrada"}
    return asdict(ocorrencia)

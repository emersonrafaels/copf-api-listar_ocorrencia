from dataclasses import dataclass

@dataclass
class Ocorrencia:
    id: int
    data_ocorrencia: str  # ISO format: YYYY-MM-DD
    tipo: str
    descricao: str
    status: str

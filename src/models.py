from pydantic import BaseModel

class Ocorrencia(BaseModel):
    id: int
    data_ocorrencia: str  # ISO format: YYYY-MM-DD
    tipo: str
    descricao: str
    status: str

from typing import List, Optional
from models import Ocorrencia

# 🔧 Mock de dados
_ocorrencias_mock: List[Ocorrencia] = [
    Ocorrencia(1, "2025-08-01", "Alerta", "Sistema fora do ar", "aberto"),
    Ocorrencia(2, "2025-08-02", "Incidente", "Erro em login", "resolvido"),
    Ocorrencia(3, "2025-08-03", "Manutenção", "Atualização programada", "em andamento"),
]

def listar_ocorrencias() -> List[Ocorrencia]:
    return _ocorrencias_mock

def buscar_ocorrencia_por_id(ocorrencia_id: int) -> Optional[Ocorrencia]:
    return next((o for o in _ocorrencias_mock if o.id == ocorrencia_id), None)

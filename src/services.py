"""
Camada de serviços para manipulação de ocorrências.
Fornece funções para listar e buscar ocorrências mockadas.
"""

from typing import List, Optional
from src.models import Ocorrencia

# Mock de dados de ocorrências
_OCORRENCIAS_MOCK: List[Ocorrencia] = [
    Ocorrencia(1, "2025-08-01", "Alerta", "Sistema fora do ar", "aberto"),
    Ocorrencia(2, "2025-08-02", "Incidente", "Erro em login", "resolvido"),
    Ocorrencia(3, "2025-08-03", "Manutenção", "Atualização programada", "em andamento"),
]

def listar_ocorrencias() -> List[Ocorrencia]:
    """
    Retorna a lista de todas as ocorrências mockadas.
    """
    return _OCORRENCIAS_MOCK.copy()

def buscar_ocorrencia_por_id(ocorrencia_id: int) -> Optional[Ocorrencia]:
    """
    Busca uma ocorrência pelo ID.
    Retorna a ocorrência se encontrada, ou None se não existir.
    """
    return next((o for o in _OCORRENCIAS_MOCK if o.id == ocorrencia_id), None)

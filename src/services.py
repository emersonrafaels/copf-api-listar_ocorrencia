"""
Camada de serviços para manipulação de ocorrências.
Fornece funções para listar e buscar ocorrências mockadas.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from typing import List, Optional
from src.models import Ocorrencia

# Mock de dados de ocorrências
_OCORRENCIAS_MOCK = [
    Ocorrencia(id=1, data_ocorrencia="2025-08-01", tipo="Alerta", descricao="Sistema fora do ar", status="aberto"),
    Ocorrencia(id=2, data_ocorrencia="2025-08-02", tipo="Incidente", descricao="Erro em login", status="resolvido"),
    Ocorrencia(id=3, data_ocorrencia="2025-08-03", tipo="Manutenção", descricao="Atualização programada", status="em andamento"),
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

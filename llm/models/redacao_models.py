from dataclasses import dataclass, asdict
from typing_extensions import override
from utils.json_utils import JsonSerializable
import json


@dataclass(frozen=True)
class Redacao(JsonSerializable):
    tema: str
    conteudo: str


@dataclass(frozen=True)
class CorrecaoCompetencia(JsonSerializable):
    nota: int
    comentario: str


@dataclass(frozen=True)
class Correcao(JsonSerializable):
    tema: str
    competencia1: CorrecaoCompetencia
    competencia2: CorrecaoCompetencia
    competencia3: CorrecaoCompetencia
    competencia4: CorrecaoCompetencia
    competencia5: CorrecaoCompetencia

    @property
    def nota_total(self) -> int:
        return (self.competencia1.nota + self.competencia2.nota
            + self.competencia3.nota + self.competencia4.nota
            + self.competencia5.nota)

    @override
    def to_json(self) -> str:
        dict_form = asdict(self)
        dict_form["notaTotal"] = self.nota_total
        return json.dumps(dict_form, indent=2, ensure_ascii=False)

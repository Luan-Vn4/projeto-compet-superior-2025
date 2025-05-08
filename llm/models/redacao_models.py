from pydantic import BaseModel, computed_field, ConfigDict


class Redacao(BaseModel):
    model_config = ConfigDict(frozen=True)
    tema: str
    conteudo: str


class CorrecaoCompetencia(BaseModel):
    model_config = ConfigDict(frozen=True)
    nota: int
    comentario: str


class Correcao(BaseModel):
    model_config = ConfigDict(frozen=True)
    tema: str
    competencia1: CorrecaoCompetencia
    competencia2: CorrecaoCompetencia
    competencia3: CorrecaoCompetencia
    competencia4: CorrecaoCompetencia
    competencia5: CorrecaoCompetencia

    @computed_field
    def nota_total(self) -> int:
        return (self.competencia1.nota + self.competencia2.nota
            + self.competencia3.nota + self.competencia4.nota
            + self.competencia5.nota)

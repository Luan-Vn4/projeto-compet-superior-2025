import type {CorrecaoCompetencia} from "./CorrecaoCompetencia.ts";

export interface Correcao {
  tema: string,
  competencia1: CorrecaoCompetencia,
  competencia2: CorrecaoCompetencia,
  competencia3: CorrecaoCompetencia,
  competencia4: CorrecaoCompetencia,
  competencia5: CorrecaoCompetencia,
}

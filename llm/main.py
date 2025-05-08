from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from models.redacao_models import Redacao, Correcao
from services.redacao_evaluator_service import RedacaoEvaluatorService

load_dotenv()
app = FastAPI()

@app.post("/correcao")
def root(redacao: Redacao) -> Correcao:
    avaliador = RedacaoEvaluatorService()
    return avaliador.evaluate(redacao)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

import httpx
from fastapi import FastAPI, Form, File, UploadFile
import uvicorn
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from models.redacao_models import Redacao, Correcao
from services.redacao_evaluator_service import RedacaoEvaluatorService
import os

load_dotenv()
app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/correcao")
async def root(
    tema: str = Form(...),
    imagem: UploadFile = File(...),
) -> Correcao:
    imagem_content = await imagem.read()

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            os.getenv('OCR_URL') + '/extracao',
            files={
                'file': (imagem.filename, imagem_content, imagem.content_type)
            }
        )

    conteudo_redacao: str = response.json()['texto_redacao']

    print(conteudo_redacao)

    avaliador = RedacaoEvaluatorService()
    redacao = Redacao(
        tema=tema,
        conteudo=conteudo_redacao,
    )

    return avaliador.evaluate(redacao)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

from fastapi import FastAPI, UploadFile, File
from models.extracao_models import RedacaoImage, TextoRedacao
import uvicorn
from dotenv import load_dotenv
from services.ocr_service import OCRService
from fastapi.responses import JSONResponse

load_dotenv()
app = FastAPI()

@app.post("/extracao")
async def root(file: UploadFile = File(...)) -> TextoRedacao:
    contents = await file.read()
    redacao_image = RedacaoImage(image_bytes=contents)

    ocr = OCRService()
    return ocr.extract_text(redacao_image)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)

import easyocr
from io import BytesIO
from models.extracao_models import RedacaoImage, TextoRedacao

class OCRService:
    def extract_text(self, redacao_image: RedacaoImage) -> TextoRedacao:
        reader = easyocr.Reader(['pt'])
        results = reader.readtext(redacao_image.get_image())

        detected_text = " ".join([text for (_, text, _) in results])
        
        return TextoRedacao(texto_redacao = detected_text)
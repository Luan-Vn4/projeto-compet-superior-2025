from pydantic import BaseModel
from PIL import Image
from io import BytesIO
import numpy as np

class RedacaoImage(BaseModel):
    image_bytes: bytes

    def get_image(self) -> np.ndarray:
        rgb_image = Image.open(BytesIO(self.image_bytes)).convert("RGB")
        np_array_image = np.array(rgb_image)
        return np_array_image

class TextoRedacao(BaseModel):
    texto_redacao: str
    
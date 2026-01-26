from pydantic import BaseModel


class Imagen(BaseModel):
    url: str | None
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "url": "https://example.com/image.jpg"
            }
        }
    }

class ImagenCreada(BaseModel):
    url: str
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "url": "https://example.com/image.jpg"
            }
        }
    }
    
class ImagenSalida(BaseModel):
    mensaje: str
    url: str
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "mensaje": "Imagen recibida correctamente",
                "url": "https://example.com/image.jpg"
            }
        }
    }
    
class ImagenEliminada(BaseModel):
    mensaje: str
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "mensaje": "Imagen eliminada correctamente"
            }
        }
    }


    
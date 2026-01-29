from pydantic import BaseModel


class Imagen(BaseModel):
    url: str | None
    precio: float
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "url": "https://example.com/image.jpg",
                "precio": 10000
            }
        }
    }

class ImagenCreada(BaseModel):
    url: str
    precio: float
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "url": "https://example.com/image.jpg",
                "precio": 10000
            }
        }
    }
    
class ImagenSalida(BaseModel):
    mensaje: str
    url: str
    precio: float
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "mensaje": "Imagen recibida correctamente",
                "url": "https://example.com/image.jpg",
                "precio": 10000
            }
        }
    }
    
class ImagenEliminada(BaseModel):
    mensaje: str
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "mensaje": "Imagen eliminada correctamente",
            }
        }
    }


    
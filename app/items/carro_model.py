from pydantic import BaseModel

class ProductoCreado(BaseModel):
    id:int
    nombre: str
    imagen: str
    precio: float
    cantidad: int = 1
    
    model_config={
        "json_schema_extra": {
            "example": {
                "id": 1,
                "nombre": "Producto 1",
                "imagen": "https://example.com/image.jpg",
                "precio": 10000,
                "cantidad": 1
            }
        }
    }
    
class ProductoActualizado(BaseModel):
    id: int
    cantidad:int
    
    model_config= {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "cantidad": 2
            }
        }
    }
    

class ProductosMensaje(BaseModel):
    mensaje: str
    
    model_config={
        "json_schema_extra": {
            "example": {
                "mensaje": "Aca Va un Mensaje"
            }
        }
    }
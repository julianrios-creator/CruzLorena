from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.items.imagen_model import Imagen, ImagenCreada, ImagenEliminada, ImagenSalida

imagen_router = APIRouter(prefix="/imagen", tags=['Imagen'])

imagen_actualizada = {
    "url": "",
    "precio": None
}

@imagen_router.get("/ver")
def ver_imagen() -> Imagen:
    return JSONResponse(content={"url": imagen_actualizada["url"], "precio": imagen_actualizada['precio']}, status_code=200)

@imagen_router.post("/agregar")
def enviar_imagen(imagen: ImagenCreada) -> ImagenSalida:
    imagen_actualizada['url'] = imagen.url
    imagen_actualizada['precio'] = imagen.precio
    return JSONResponse(content={"mensaje": "Imagen recibida correctamente", "url": imagen_actualizada["url"], "precio": imagen_actualizada["precio"]}, status_code=201)

@imagen_router.delete("/eliminar")
def eliminar_imagen() -> ImagenEliminada:
    imagen_actualizada['url'] = ""
    imagen_actualizada['precio'] = None
    return JSONResponse(content={"mensaje": "Imagen eliminada correctamente"}, status_code=200)
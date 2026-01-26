from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.items.carro_model import ProductoActualizado, ProductoCreado, ProductosMensaje

carro_router = APIRouter(prefix="/carrito", tags=['Productos'])

carrito = []

@carro_router.get("/ver")
def ver_carrito() -> List[ProductoCreado]:
    return JSONResponse(content=carrito, status_code=200)

@carro_router.post("/agregar")
def agregar_carrito(producto: ProductoCreado) -> List[ProductoCreado]:
    carrito.append(producto)
    return JSONResponse(content=carrito, status_code=201)

@carro_router.put("/actualizar")
def actualizar_carrito(producto_actualizado: ProductoActualizado) -> ProductosMensaje:
    for producto in carrito:
        if producto.id == producto_actualizado.id:
            producto.cantidad = producto_actualizado.cantidad
            break
    return JSONResponse(content={"mensaje": "Producto actualizado correctamente"})

@carro_router.delete("/eliminar/{id}")
def eliminar_producto_individual(id: int) -> ProductosMensaje:
    carrito = [producto for producto in carrito if producto.id != id]
    return JSONResponse(content={"mensaje": "Producto eliminado correctamente"})

@carro_router.delete("/eliminar")
def eliminar_carrito()->ProductosMensaje:
    carrito.clear()
    return JSONResponse(content={"mensaje": "Producto eliminado correctamente"})
    




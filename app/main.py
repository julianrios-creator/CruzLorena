from fastapi import FastAPI

from app.routes.carro_router import carro_router
from app.routes.imagen_router import imagen_router


app = FastAPI()

app.include_router(imagen_router)
app.include_router(carro_router)

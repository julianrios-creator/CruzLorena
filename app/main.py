from fastapi import FastAPI

from app.routes.carro_router import carro_router
from app.routes.imagen_router import imagen_router
from app.utils.cors import add_cors_middleware
from app.utils.http_error_handler import HTTPErrorHandler


app = FastAPI()

# Cors Middleware
add_cors_middleware(app)
app.add_middleware(HTTPErrorHandler)

app.include_router(imagen_router)
app.include_router(carro_router)

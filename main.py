from fastapi import FastAPI, Query, Path
from models.product import Product
from routers.product import router as product_router


app = FastAPI()

# Creo Rutas
@app.get('/')
def message():
    return "Hola Mundo!"

app.include_router(product_router)

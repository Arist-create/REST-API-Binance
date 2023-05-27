from fastapi import FastAPI
from src.routes import create_orders_route, get_orders_route, cancel_orders_route


app = FastAPI()


app.include_router(create_orders_route.router)
app.include_router(get_orders_route.router)
app.include_router(cancel_orders_route.router)

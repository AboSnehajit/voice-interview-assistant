from fastapi import FastAPI
from app.routers.health_router import router

app= FastAPI(title="Voice Interview Assistant ")

app.include_router(router)

@app.get("/")
def root():
    return{"message":"Interview  backend running successfully!"}

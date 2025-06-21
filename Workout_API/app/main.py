from fastapi import FastAPI
from app.routers import categoria_router, centro_treinamento_router, atleta_router

app = FastAPI(title="WorkoutAPI")

app.include_router(categoria_router.router, prefix="/categoria", tags=["Categoria"])
app.include_router(centro_treinamento_router.router, prefix="/centro_treinamento", tags=["Centro de Treinamento"])
app.include_router(atleta_router.router, prefix="/atleta", tags=["Atleta"])

@app.get("/")
async def root():
    return {"message": "WorkoutAPI está no ar!"}




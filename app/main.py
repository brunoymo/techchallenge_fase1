from fastapi import FastAPI
from app.routes import producao, processamento, comercializacao, importacao, exportacao

app = FastAPI(
    title="Embrapa Viticultura API",
    description="API para consulta de dados vitivinícolas via CSVs da Embrapa",
    version="2.0.0"
)

# Registrar endpoints
app.include_router(producao.router)
app.include_router(processamento.router)
app.include_router(comercializacao.router)
app.include_router(importacao.router)
app.include_router(exportacao.router)
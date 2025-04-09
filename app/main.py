from fastapi import FastAPI, HTTPException
from app.routes import producao, processamento, comercializacao, importacao, exportacao
from app.auth import create_access_token

app = FastAPI(
    title="Embrapa Viticultura API",
    description="API para consulta de dados vitivinícolas via CSVs da Embrapa",
    version="2.0.0"
)

# Rota inicial
@app.get("/", summary="Página inicial da API")
async def home():
    return {
        "message": "Bem-vindo à API de Vitivinicultura!",
        "endpoints": [
            "/producao",
            "/processamento",
            "/comercializacao",
            "/importacao",
            "/exportacao"
        ]
    }

# Registrar endpoints
app.include_router(producao.router)
app.include_router(processamento.router)
app.include_router(comercializacao.router)
app.include_router(importacao.router)
app.include_router(exportacao.router)

# Rota de login para gerar token JWT
@app.post("/login", summary="Gerar Token JWT")
async def login(username: str, password: str):
    try:
        if username == "admin" and password == "password":
            token = create_access_token({"sub": username})
            return {"access_token": token, "token_type": "bearer"}
        raise HTTPException(status_code=401, detail="Invalid credentials")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
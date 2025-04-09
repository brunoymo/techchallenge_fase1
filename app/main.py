from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.auth import create_access_token, verify_token
from app.routes import producao, processamento, comercializacao, importacao, exportacao
from pydantic import BaseModel, Field
from datetime import timedelta
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

# Cria a instância da aplicação FastAPI
app = FastAPI(
    title="Embrapa Viticultura API",
    description="API para consulta de dados vitivinícolas via CSVs da Embrapa",
    version="2.0.0",
    docs_url=None,  # Desativa a documentação padrão
    redoc_url=None  # Desativa a documentação ReDoc
)

# Configuração de autenticação
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# Modelo Pydantic para login com exemplos e descrições
class LoginRequest(BaseModel):
    username: str = Field(..., description="Nome de usuário para autenticação", example="admin")
    password: str = Field(..., description="Senha do usuário", example="password")

    class Config:
        schema_extra = {
            "example": {
                "username": "admin",
                "password": "password"
            }
        }

# Configuração personalizada para aceitar JWT no Swagger
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
    )

# Função para personalizar o esquema OpenAPI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    # Gera o esquema OpenAPI padrão do FastAPI
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    
    # Adiciona o campo 'openapi' com a versão 3.0.0
    openapi_schema["openapi"] = "3.0.0"
    
    # Adiciona o esquema de segurança JWT sem sobrescrever os outros componentes
    if "components" not in openapi_schema:
        openapi_schema["components"] = {}
    if "securitySchemes" not in openapi_schema["components"]:
        openapi_schema["components"]["securitySchemes"] = {}
    
    openapi_schema["components"]["securitySchemes"]["BearerAuth"] = {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
    }
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Aplica a função custom_openapi ao app
app.openapi = custom_openapi

# Endpoint para login e geração do token JWT
@app.post("/login", summary="Gerar Token JWT")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Verifica as credenciais (simples exemplo hardcoded)
    if form_data.username != "admin" or form_data.password != "password":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Gera o token JWT
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Exemplo de endpoint protegido
@app.get("/protected", summary="Rota protegida")
async def protected_route(token: dict = Depends(verify_token)):
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"message": f"Olá, {token['sub']}"}

# Registrar os endpoints
app.include_router(producao.router)
app.include_router(processamento.router)
app.include_router(comercializacao.router)
app.include_router(importacao.router)
app.include_router(exportacao.router)

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
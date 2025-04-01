from fastapi import APIRouter, HTTPException
from app.scraper import EmbrapaScraper

router = APIRouter(prefix="/comercializacao", tags=["Comercializacao"])

@router.get("/", summary="Dados de comercialização vitivinícola")
async def get_producao():
    scraper = EmbrapaScraper()
    data = scraper.get_data("comercializacao")
    if "error" in data:
        raise HTTPException(status_code=500, detail=data["error"])
    return data
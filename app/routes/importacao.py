from fastapi import APIRouter, HTTPException
from app.scraper import EmbrapaScraper

router = APIRouter(prefix="/importacao", tags=["Importacao"])

@router.get("/", summary="Dados de importação vitivinícola")
async def get_producao():
    scraper = EmbrapaScraper()
    data = scraper.get_data("importacao")
    if "error" in data:
        raise HTTPException(status_code=500, detail=data["error"])
    return data
from fastapi import APIRouter, HTTPException
from app.scraper import EmbrapaScraper

router = APIRouter(prefix="/producao", tags=["Produção"])

@router.get("/", summary="Dados de produção vitivinícola")
async def get_producao():
    scraper = EmbrapaScraper()
    data = scraper.get_data("producao")
    if "error" in data:
        raise HTTPException(status_code=500, detail=data["error"])
    return data
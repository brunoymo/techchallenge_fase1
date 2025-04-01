from fastapi import APIRouter, HTTPException
from app.scraper import EmbrapaScraper

router = APIRouter(prefix="/exportacao", tags=["Exportacao"])

@router.get("/", summary="Dados de exportação vitivinícola")
async def get_producao():
    scraper = EmbrapaScraper()
    data = scraper.get_data("exportacao")
    if "error" in data:
        raise HTTPException(status_code=500, detail=data["error"])
    return data
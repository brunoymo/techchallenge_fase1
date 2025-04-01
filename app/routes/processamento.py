from fastapi import APIRouter, HTTPException
from app.scraper import EmbrapaScraper

router = APIRouter(prefix="/processamento", tags=["Processamento"])

@router.get("/", summary="Dados de processamento vitivinícola")
async def get_producao():
    scraper = EmbrapaScraper()
    data = scraper.get_data("processamento")
    if "error" in data:
        raise HTTPException(status_code=500, detail=data["error"])
    return data
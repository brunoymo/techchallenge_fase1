from fastapi import APIRouter, HTTPException, Depends
from app.scraper import EmbrapaScraper
from app.auth import verify_token

router = APIRouter(prefix="/producao", tags=["Produção"])

@router.get("/", summary="Dados de produção vitivinícola")
async def get_producao(token: dict = Depends(verify_token)):
    scraper = EmbrapaScraper()
    data = scraper.get_data("producao")
    if "error" in data:
        raise HTTPException(status_code=500, detail=data["error"])
    return data
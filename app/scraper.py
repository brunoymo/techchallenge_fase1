import requests
import pandas as pd
from io import StringIO

class EmbrapaScraper:
    CSV_URLS = {
        "producao": "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv",
        "processamento": "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
        "comercializacao": "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
        "importacao": "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
        "exportacao": "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv"
    }

    def get_data(self, tipo: str):
        try:
            response = requests.get(self.CSV_URLS[tipo], timeout=10)
            response.encoding = 'utf-8'
            df = pd.read_csv(StringIO(response.text), sep=';', skipfooter=2, engine='python')
            return df.dropna().to_dict(orient='records')
        except Exception as e:
            return {"error": str(e)}
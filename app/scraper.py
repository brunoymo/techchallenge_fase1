import requests
import pandas as pd
from io import StringIO
from pathlib import Path

class EmbrapaScraper:
    CSV_URLS = {
        "producao": "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv",
        "processamento": "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
        "comercializacao": "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
        "importacao": "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
        "exportacao": "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv"
    }

    DATA_DIR = Path("data")
    DATA_DIR.mkdir(exist_ok=True)

    def save_to_file(self, tipo: str, content: str):
        file_path = self.DATA_DIR / f"{tipo}.csv"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return file_path

    def get_data(self, tipo: str):
        try:
            response = requests.get(self.CSV_URLS[tipo], timeout=10)
            response.encoding = 'utf-8'
            self.save_to_file(tipo, response.text)  # Salva o arquivo localmente
            df = pd.read_csv(StringIO(response.text), sep=';', skipfooter=2, engine='python')
            return df.dropna().to_dict(orient='records')
        except Exception as e:
            return {"error": str(e)}
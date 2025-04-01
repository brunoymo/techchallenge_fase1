 `README.md` para o projeto da API Embrapa:

```markdown
# API de Dados Vitivinícolas da Embrapa

API REST para consulta dos dados públicos de vitivinicultura da Embrapa, construída com FastAPI.

## Endpoints

| Endpoint           | Descrição                     | Exemplo de Uso                     |
|--------------------|-------------------------------|------------------------------------|
| `/producao`        | Dados de produção             | `GET /producao`                    |
| `/processamento`   | Dados de processamento        | `GET /processamento`               |
| `/comercializacao` | Dados de comercialização      | `GET /comercializacao`             |
| `/importacao`      | Dados de importação           | `GET /importacao`                  |
| `/exportacao`      | Dados de exportação           | `GET /exportacao`                  |

# Como Executar

## Pré-requisitos
- Python 3.8+
- Pip

## Instalação Local
```bash

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute a API
uvicorn app.main:app --reload
```

Acesse a documentação interativa:  
🔹 [http://localhost:8000/docs](http://localhost:8000/docs)  
🔹 [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Exemplo de Request
```bash
curl -X 'GET' \
  'http://localhost:8000/producao' \
  -H 'accept: application/json'
```

## Tecnologias Utilizadas
- [FastAPI](https://fastapi.tiangolo.com/) - Framework para construção da API
- [Pandas](https://pandas.pydata.org/) - Processamento de dados
- [Requests](https://docs.python-requests.org/) - Requisições HTTP
- [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI

## Fonte dos Dados
Dados obtidos diretamente dos CSVs públicos da [Embrapa Vitivinicultura](http://vitibrasil.cnpuv.embrapa.br/).

## Como Contribuir
1. Faça um fork do projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença
Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---
> Desenvolvido como parte do Tech Challenge FIAP - Machine Learning Engineering
```

### Recursos incluídos:
1. **Badges** (adicione manualmente depois no GitHub)
2. **Tabela de endpoints** formatada
3. **Instruções para diferentes SOs** (Linux/Mac/Windows)
4. **Exemplo de request** com curl
5. **Seção de contribuição** padrão
6. **Links** para documentação das tecnologias

### Personalize com:
```markdown
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68-green.svg)](https://fastapi.tiangolo.com)
``` 
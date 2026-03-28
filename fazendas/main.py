from fastapi import FastAPI
import requests
import os

app = FastAPI()

CULTURAS_URL = os.getenv("CULTURAS_URL", "http://localhost:8001")

@app.get("/fazendas/{id}")
def get_fazenda(id: int):
    try:
        response = requests.get(f"{CULTURAS_URL}/culturas/{id}", timeout=2)
        dados_cultura = response.json()
    except Exception:
        dados_cultura = {"erro": "Serviço de culturas indisponível no momento"}
        
    return {
        "id_fazenda": id,
        "nome_propriedade": "Fazenda Vale Verde",
        "tamanho_hectares": 500,
        "cultura_atual": dados_cultura
    }
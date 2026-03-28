from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/culturas/{id}")
def get_cultura(id: int):
    time.sleep(5) # <-- Aqui está o atraso proposital de 5 segundos
    return {
        "id": id,
        "nome": "Soja",
        "tempo_colheita_dias": 120,
        "epoca_ideal": "Primavera/Verão"
    }
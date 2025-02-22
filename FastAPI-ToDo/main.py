from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def home():
    with open('dados.json', 'r', encoding='utf-8') as arquivo_json:
        dados = json.load(arquivo_json) 
    return dados
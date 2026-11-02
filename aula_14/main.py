from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import requests

app = FastAPI(
    title="API Casa de Suco 🧃",
    version="1.0.0",
    description="API para gerenciar sucos e calcular informações nutricionais integrada à Fruityvice."
)

# Base de dados em memória
sucos_db = {}
contador_id = 1

# Modelos Pydantic
class SucoCreate(BaseModel):
    nome: str
    frutas: List[str]
    tem_gosto_de: str

class SucoUpdate(BaseModel):
    nome: Optional[str] = None
    frutas: Optional[List[str]] = None
    tem_gosto_de: Optional[str] = None

FRUITYVICE_URL = "https://www.fruityvice.com/api/fruit/"

def consultar_fruta_fruityvice(nome_fruta: str):
    """Consulta a API externa Fruityvice com tratamento de erros 404."""
    try:
        response = requests.get(f"{FRUITYVICE_URL}{nome_fruta.lower()}")
    except requests.RequestException:
        raise HTTPException(status_code=500, detail="Erro de conexão com o serviço externo Fruityvice.")
    
    if response.status_code == 404:
        raise HTTPException(
            status_code=404, 
            detail=f"A fruta '{nome_fruta}' não foi encontrada na base de dados da Fruityvice."
        )
    elif response.status_code != 200:
        raise HTTPException(status_code=500, detail="Erro inesperado ao consultar a API Fruityvice.")
        
    return response.json()

@app.get("/")
def inicio():
    return {"mensagem": "Bem-vindo à API Casa de Suco! Acesse /docs para ver a documentação."}

# 1. Consulta de frutas GET /frutas/{nome}
@app.get("/frutas/{nome}")
def consultar_fruta(nome: str):
    dados = consultar_fruta_fruityvice(nome)
    nutricoes = dados.get("nutritions", {})
    return {
        "nome": dados.get("name"),
        "calorias": nutricoes.get("calories", 0),
        "acucar": nutricoes.get("sugar", 0)
    }

# 2. Cadastro de sucos POST /sucos
@app.post("/sucos", status_code=201)
def cadastrar_suco(suco: SucoCreate):
    global contador_id
    total_calorias = 0.0
    total_acucar = 0.0

    for fruta in suco.frutas:
        dados = consultar_fruta_fruityvice(fruta)
        nutricoes = dados.get("nutritions", {})
        total_calorias += nutricoes.get("calories", 0)
        total_acucar += nutricoes.get("sugar", 0)

    novo_suco = {
        "id": contador_id,
        "nome": suco.nome,
        "frutas": suco.frutas,
        "tem_gosto_de": suco.tem_gosto_de,
        "total_calorias": round(total_calorias, 2),
        "total_acucar": round(total_acucar, 2)
    }
    
    sucos_db[contador_id] = novo_suco
    contador_id += 1
    return novo_suco

# 3. Listagem de sucos GET /sucos
@app.get("/sucos")
def listar_sucos():
    return list(sucos_db.values())

# Desafio Bônus: Rota PUT /sucos/{id}
@app.put("/sucos/{id}")
def atualizar_suco(id: int, suco_up: SucoUpdate):
    if id not in sucos_db:
        raise HTTPException(status_code=404, detail=f"Suco com ID {id} não encontrado.")

    suco_existente = sucos_db[id]

    if suco_up.nome is not None:
        suco_existente["nome"] = suco_up.nome
    if suco_up.tem_gosto_de is not None:
        suco_existente["tem_gosto_de"] = suco_up.tem_gosto_de
    
    if suco_up.frutas is not None:
        total_calorias = 0.0
        total_acucar = 0.0
        
        for fruta in suco_up.frutas:
            dados = consultar_fruta_fruityvice(fruta)
            nutricoes = dados.get("nutritions", {})
            total_calorias += nutricoes.get("calories", 0)
            total_acucar += nutricoes.get("sugar", 0)
            
        suco_existente["frutas"] = suco_up.frutas
        suco_existente["total_calorias"] = round(total_calorias, 2)
        suco_existente["total_acucar"] = round(total_acucar, 2)

    return suco_existente
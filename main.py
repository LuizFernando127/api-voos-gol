from fastapi import FastAPI

# Inicializa o aplicativo
app = FastAPI(title="API de Voos - Simulação GOL")

# Banco de dados fictício
voos_mock = [
    {"voo": "G3 1540", "destino": "Rio de Janeiro (SDU)", "status": "No Horário"},
    {"voo": "G3 1022", "destino": "Salvador (SSA)", "status": "Embarque Próximo"},
    {"voo": "G3 2100", "destino": "Brasília (BSB)", "status": "Atrasado"}
]

# Rota principal (Home)
@app.get("/")
def home():
    return {"mensagem": "Bem-vindo ao sistema de consulta de voos!"}

# Rota para listar todos os voos
@app.get("/voos")
def listar_voos():
    return {"voos": voos_mock}

# Rota para buscar um voo específico
@app.get("/voos/{numero_voo}")
def buscar_voo(numero_voo: str):
    for voo in voos_mock:
        if voo["voo"].replace(" ", "").lower() == numero_voo.replace(" ", "").lower():
            return voo
    return {"erro": "Voo não encontrado"}
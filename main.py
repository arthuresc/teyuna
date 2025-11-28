from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.produtos_router import router as produtos_router

app = FastAPI(
    title="API de Produtos",
    description="Uma API RESTful para gerenciar produtos",
    version="1.0.0"
)
# É pra colocar a origin das requisições aqui e eu tava sendo negligente colocando a porta da própria API
origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(produtos_router)

# Rota raiz
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Produtos!"}

# Health check
@app.get("/health")
def health_check():
    return {"status": "healthy"}
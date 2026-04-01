from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routers.produtos_router import router as produtos_router
from sqlalchemy.orm import Session
from database.session import get_db
from sqlalchemy import text


app = FastAPI(
    title="API de Produtos",
    description="Uma API RESTful para gerenciar produtos",
    version="1.0.0"
)
# É pra colocar a origin das requisições aqui e eu tava sendo negligente colocando a porta da própria API
origins = [
    "http://127.0.0.1:5174",
    "http://localhost:5174",
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

# Health check: db
@app.get("/health/db")
def check_db(db: Session = Depends(get_db)):
    try:
      db.execute(text("SELECT 1"))
      return {"status": "healthy"}
    except Exception as e:
      return {"status": "error", "detail": str(e)}
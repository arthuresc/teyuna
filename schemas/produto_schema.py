from pydantic import BaseModel
from typing import Optional

# Schema para criação de produto
class ProdutoCreate(BaseModel):
    nome: str
    preco: float
    descricao: Optional[str] = None

# Schema para resposta da API
class ProdutoResponse(BaseModel):
    id: int
    nome: str
    preco: float
    descricao: Optional[str] = None
    
    # Isso permite que o FastAPI converta automaticamente de ORM para JSON
    class Config:
        from_attributes = True
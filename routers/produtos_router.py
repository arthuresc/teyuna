from fastapi import APIRouter, HTTPException
from schemas.produto_schema import ProdutoResponse
from schemas.produto_schema import ProdutoCreate
from database.fake_db import get_produtos, get_produto_por_id
import logging

# Cria um roteador específico para produtos
router = APIRouter(prefix="/produtos", tags=["produtos"])

# Rota GET /produtos/
@router.get("/", response_model=list[ProdutoResponse])
def listar_produtos():
    """
    Retorna todos os produtos
    """
    produtos = get_produtos()
    return produtos

# Rota GET /produtos/{id}
@router.get("/{produto_id}", response_model=ProdutoResponse)
def obter_produto(produto_id: int):
    """
    Retorna um produto específico pelo ID
    """
    produto = get_produto_por_id(produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

# Rota POST /produtos/
@router.post("/", response_model=ProdutoResponse)
def criar_produto(produto: ProdutoCreate):
    """
    Cria um novo produto
    """
    # Aqui você salvaria no banco de dados real
    novo_produto = {
        "id": len(get_produtos()) + 1,
        "nome": produto.nome,
        "preco": produto.preco,
        "descricao": produto.descricao
    }
    get_produtos().append(novo_produto)
    return novo_produto
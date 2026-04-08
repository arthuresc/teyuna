from fastapi import APIRouter, HTTPException
from schemas.produto_schema import ProdutoResponse
from schemas.produto_schema import ProdutoCreate
from database.fake_db import get_produtos, get_produto_por_id

# Cria um roteador específico para produtos
router = APIRouter(prefix="/produtos", tags=["produtos"])

# Rota GET /produtos/
@router.get("/", response_model=list[ProdutoResponse])
async def list_products():
    """
    Retorna todos os produtos
    """
    produtos = get_produtos()
    return produtos

# Rota GET /produtos/{id}
@router.get("/{produto_id}", response_model=ProdutoResponse)
async def get_product(product_id: int):
    """
    Retorna um produto específico pelo ID
    """
    product = get_produto_por_id(product_id)
    if not product:
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
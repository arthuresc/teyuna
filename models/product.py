from sqlalchemy import Column, Integer, String, Numeric, Float, ForeignKey, Boolean, Enum
from sqlalchemy.sql import func
from database.base import Base, BaseMixins
from .kit_component import KitComponent
import enum

class ProductType(enum.Enum):
    SIMPLE = "simple"
    KIT = "kit"


# Modelo do banco de dados
class Product(BaseMixins, Base):
    __tablename__ = "products"
    
    name = Column(String(100), nullable=False, index=True)
    price = Column(Float, nullable=False)
    description = Column(String(500), nullable=True)
    code = Column(String(50), nullable=False, index=True, unique=True)
    sku = Column(String(50), unique=True, nullable=True)
    # Ele faz um enumaration da classe ProductType aonde só existem 2 valores SIMPLE que é "simple" e vai manter uma espécie de chave valor mas sem 
    type = Column(Enum(ProductType), nullable=False)
    is_active = Column(Boolean, nullable=False)
    
    
    # Relacionamentos serão importados após a definição de KitComponent
    # para evitar importação circular.

    __table_args__ = (
        Index("idx_products_type_active", "type", "is_active"),
    )

    @hybrid_property
    def is_kit(self):
        return self.type == ProductType.KIT
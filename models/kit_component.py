from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Table, Index, CheckConstraint
from sqlalchemy.sql import func
from database.base import Base, BaseMixins
# Modelo do banco de dados
class KitComponent(BaseMixins, Base):
    __tablename__ = "kit_components"
    
    kit_id = Column(Inteer, ForeignKey("products.id", ondelete="CASCADE"), primary_key=True)
    component_id = Column(Inteer, ForeignKey("products.id", ondelete="RESTRICT"), primary_key=True)
    
    
    default_quantity = Column(Integer, nullable=False)
    is_optional = Column(Boolean, default=False, nullable=False)
    sort_order = Column(Integer, default=0, nullable=False)
    
    kit = relationship(
        "Product",
        foreign_keys=[kit_id],
        back_populates="kit_component_associations",
    )
    
    component = relationship(
        "Product",
        foreign_keys=[component_id],
        back_populates="component_associations"
    )
    
    __table_args__ = (
        CheckConstraint("default_quantity > 0", name="ck_kit_component_positive_quantity"),
        Index("idx_kit_components_component", "component_id"),
    )
    # Herdados de produto
    # name = Column(String(100), nullable=False, index=True)
    # price = Column(Float, nullable=False)
    # description = Column(String(500), nullable=True)
    # id = Column(Integer, primary_key=True, index=True)
    kit_id = Column(Integer, nullable=False, index=True)
    
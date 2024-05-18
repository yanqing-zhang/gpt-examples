from database.db_connection import db
from sqlalchemy import Column, Integer, String, DateTime, Double
from datetime import datetime

class Sku(db.Model):
    """
    商品实体模型封装 ORM映射
    """
    id = Column(Integer, primary_key=True)
    order_id = Column(String(80), unique=True, nullable=False)
    sku_name = Column(String(120))
    sku_id = Column(String(120), unique=True, nullable=False)
    sku_price = Column(Double)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now)
    yn = Column(db.Integer, default=1)

    def __repr__(self):
        return f"Sku('{self.sku_id}', '{self.sku_name}')"

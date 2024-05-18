from database.db_connection import db
from sqlalchemy import Column, Integer, String, DateTime, Double
from datetime import datetime
import json

class Orders(db.Model):
    """
    订单实体模型封装 ORM映射
    """
    id = Column(Integer, primary_key=True)
    order_id = Column(String(80), unique=True, nullable=False)
    order_total_amount = Column(Double)
    order_status = Column(Integer)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now)
    yn = Column(db.Integer, default=1)

    def __repr__(self):
        return f"{{\'order_id\':{self.order_id}, \'order_total_amount\':{self.order_total_amount}, \'order_status\':{self.order_status}, \'create_at\':{self.create_at}, \'update_at\':{self.update_at}, \'yn\':{self.yn}}}"

    def to_dict(self):
        return self.__dict__

    def to_json(self,data):
        order_dict = {}
        order_dict['order_id'] = data.order_id
        order_dict['order_total_amount'] = data.order_total_amount
        order_dict['order_status'] = data.order_status
        order_dict['create_at'] = data.create_at.strftime("%Y-%m-%d %H:%M:%S")
        order_dict['update_at'] = data.update_at.strftime("%Y-%m-%d %H:%M:%S")
        order_dict['yn'] = data.yn
        j = json.dumps(order_dict)
        return j
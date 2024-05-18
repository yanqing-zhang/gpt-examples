from database.db_connection import db
from model.orders import Orders
import json,datetime

class OrderDao:
    """
    数据操作层:DAO（Data Access Object）
    """

    def save(self,orders):
        db.session.add(orders)
        db.session.commit()

    def del_order(self, orders):
        Orders.query.filter(Orders.order_id == orders.order_id).delete()
        db.session.commit()

    def update_order(self, orders):
        data = db.session.query(Orders).filter(Orders.order_id == orders.order_id).first()
        if data is None:
            return
        if data.order_total_amount != orders.order_total_amount:
            data.order_total_amount = orders.order_total_amount
        if data.order_status != orders.order_status:
            data.order_status = orders.order_status
        data.update_at = datetime.datetime.now()
        db.session.commit()

    def get_one(self, orders):
        data = Orders.query.filter(Orders.order_id == orders.order_id).first()
        return data

    def get_all(self,orders, page_size, page_index):
        ps = int(page_size)
        pi = int(page_index)
        # .outerjoin(Sku, Orders.order_id == Sku.order_id)
        data = db.session.query(Orders)\
            .filter(Orders.order_status == orders.order_status).limit(ps).offset((pi- 1) * ps).all()
        db.session.commit()
        print(f'data:{data}')
        print("-------------------------------")
        # print(f'data`s len:{len(data)}')
        return data

    def query_all(self,orders):
        # .outerjoin(Sku, Orders.order_id == Sku.order_id)
        data = db.session.query(Orders)\
            .filter(Orders.order_status == orders.order_status).all()
        db.session.commit()
        print(f'data:{data}')
        print("-------------------------------")
        return data
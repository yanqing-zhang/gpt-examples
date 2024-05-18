from flask import Flask
from dao.order_dao import OrderDao
from model.orders import Orders
from web.orders_web import launch_gradio
import database.db_connection as db

app = Flask(__name__)
# 注册数据库
app = db.config_app()

# 防止出现RuntimeError: Working outside of application context.
app.app_context().push()

# @app.route("/query_all_comstomers")
# def query_all_comstomers():
#     table_components.launch()

if __name__ == '__main__':
    # app.run()
    launch_gradio()
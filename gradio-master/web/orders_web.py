import gradio as gr
from dao.order_dao import OrderDao
from model.orders import Orders
import pandas as pd
def get_orders():
    orderDao = OrderDao()
    orders = Orders()
    orders.order_status = 1
    data = orderDao.query_all(orders)
    return data


def process_table(df):
    # Process the DataFrame here
    return df.describe()


def launch_gradio():
    iface = gr.Interface(
        fn=process_table,
        input=gr.inputs.DataFrame(
            label='Table',
            interactive=True,
            wrap=True
        ),
        output="text"
    )
    iface.launch()


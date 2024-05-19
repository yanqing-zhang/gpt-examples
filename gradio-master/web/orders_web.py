import gradio as gr
from dao.order_dao import OrderDao
from model.orders import Orders
import pandas as pd
from pandas import DataFrame
import json
def get_orders():
    # orderDao = OrderDao()
    # orders = Orders()
    # orders.order_status = 1
    # datas = orderDao.query_all(orders)
    data = {
        'Fruit': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
        'Quantity': [15, 23, 9, 4, 18],
        'Price': [0.35, 0.40, 0.50, 0.55, 0.75],
        'Sale_date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03']
    }

    return data
def launch_gradio():
    df = pd.DataFrame({
        "A": [14, 4, 5, 4, 1],
        "B": [5, 2, 54, 3, 2],
        "C": [20, 20, 7, 3, 8],
        "D": [14, 3, 6, 2, 6],
        "E": [23, 45, 64, 32, 23]
    })
    styler = df.style.highlight_max(color='lightgreen', axis=0)

    # Displaying the styled dataframe in Gradio
    with gr.Blocks() as demo:
        gr.DataFrame(styler)
    demo.launch()



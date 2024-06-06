import gradio as gr
import os

cur_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(os.path.dirname(cur_path), 'gradio-master')

def get_order_info(name,phone,sku_name,order_id):
    order_str = f"""手机号为:{phone}的{name},他的订单:{order_id},他买了{sku_name}"""
    return order_str
"""
examples引入csv失败，后面再研究一下，还没有看到配置细节或示例
"""
demo = gr.Interface(
    fn=get_order_info,
    inputs=[gr.Textbox(),gr.Textbox(),gr.Textbox(),gr.Textbox()],
    outputs=gr.Textbox(lines=4),
    examples=f"{data_path}\datas\log.csv"
)

demo.launch()

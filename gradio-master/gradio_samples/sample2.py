import gradio as gr
import cv2

"""
cv2安装
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python
"""

def turn_gray(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

iface = gr.Interface(fn=turn_gray, inputs=gr.Image(), outputs="image")


iface.launch()
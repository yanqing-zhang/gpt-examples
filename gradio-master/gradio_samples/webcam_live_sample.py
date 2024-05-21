import gradio as gr
import numpy as np
"""
调取摄像头gr.Image(sources=["webcam"], streaming=True)
live=True可以实时得到结果
"""
def flip(im):
    return np.flipud(im)

demo = gr.Interface(
    flip,
    gr.Image(sources=["webcam"], streaming=True),
    "image",
    live=True
)
demo.launch()
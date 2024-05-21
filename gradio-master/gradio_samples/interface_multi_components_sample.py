import gradio as gr

def turn_values(name, temprature,fruit,file_path):
    return name, temprature, fruit, file_path

iface = gr.Interface(
    fn=turn_values,
    inputs=[
        gr.Textbox(label="姓名"),
        gr.Slider(label="温度", value=2, minimum=1, maximum=20, step=1),
        gr.Checkbox(label="水果"),
        gr.Image(label="上传图片")

    ],
    outputs=[
        gr.Textbox(),
        gr.Textbox(),
        gr.Textbox(),
        gr.Textbox()
    ]
)

iface.launch()
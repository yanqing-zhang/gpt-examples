import gradio as gr

def greet(name):
    return "Hello" + name

# iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(lines=5, placeholder="请输入姓名", label="姓名"),
    outputs=gr.Textbox(label="问候")
)
iface.launch()
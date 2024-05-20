import gradio as gr

def file_path(input):
    return input

iface = gr.Interface(
    fn=file_path,
    inputs=gr.Audio(sources=["microphone"], type="filepath"),
    outputs="text"
)

iface.launch()
import gradio as gr

def generate_fake_image(prompt, seed, initial_image=None):
    return f"Used seed: {seed}", "https://dummyimage.com/300/09f.png"
"""
gr.Interface的additional_inputs属性用于折叠显示包含的组件，默认状态是折叠不显示的
"""
demo = gr.Interface(
    generate_fake_image,
    inputs=["textbox"],
    outputs=["textbox", "image"],
    additional_inputs=[
        gr.Slider(0, 1000),
        "image"
    ]
)

demo.launch()


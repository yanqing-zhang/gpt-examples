import gradio as gr
from transformers import pipeline
import os
"""
遇到以下通信问题，如果通过环境变量设置及代理解决
requests.exceptions.SSLError: (MaxRetryError("HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /t5-base/resolve/main/config.json (Caused by SSLError(SSLZeroReturnError(6, 'TLS/SSL connection has been closed (EOF) (_ssl.c:1135)')))"), '(Request ID: dd3aa975-36a8-4681-9cc2-86e199e86a5a)')
"""
os.environ['CURL_CA_BUNDLE'] = ''
os.environ["http_proxy"] = "http://127.0.0.1:10794"
os.environ["https_proxy"] = "http://127.0.0.1:10794"
"""======================================================="""
pipe = pipeline("translation", model="t5-base")

def translate(text):
    return pipe(text)[0]["translation_text"]

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            english = gr.Textbox(label="English text")
            translate_btn = gr.Button(value="Translate")
        with gr.Column():
            de = gr.Textbox(label="de Text")
    translate_btn.click(translate, inputs=english, outputs=de)
    examples = gr.Examples(examples=["I went to the supermarket yesterday.", "Helen is a good swimmer."],
                           inputs=[english])


demo.launch()
import sys
import os
import gradio as gr

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import LOG
from translator import PDFTranslator
from configs.translate_config import TranslationConfig

def translation(input_file, source_language, target_language):
    LOG.debug(f"[翻译任务]\n源文件: {input_file.name}\n源语言: {source_language}\n目标语言: {target_language}")
    output_file_path = PDFTranslator.translate_pdf(
        input_file.name,
        source_language=source_language,
        target_language=target_language)
    return output_file_path

def launch_gradio():
    iface = gr.Interface(
        fn=translation,
        title="OpenAI-Translator v2.0(PDF 电子书翻译)",
        inputs=[
            gr.File(label="上传PDF文件"),
            gr.Textbox(label="源语言", placeholder="English", value="English"),
            gr.Textbox(label="目标语言", placeholder="Chinese", value="Chinese")
        ],
        outputs=[
            gr.File(label="下载翻译文件")
        ],
        allow_flagging="vever"
    )
    iface.launch(share=True, server_name="0.0.0.0")

def initialize_translator():
    config = TranslationConfig()
    config.

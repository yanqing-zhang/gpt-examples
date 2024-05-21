from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
import os
class TranslatorMultiLanguageOpenAI:

    def chat(self):
        template = (
            """You are a translation expert, proficient in various languages. \n
            Translates {source_language} to {target_language}."""
        )
        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        human_template = "{text}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
        m_chat_prompt_template = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )
        client = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        m_translation_chain = LLMChain(llm=client, prompt=m_chat_prompt_template)
        re1 = m_translation_chain.run({
            "source_language": "Chinese",
            "target_language": "English",
            "text": "我喜欢学习大语言模型，轻松简单又愉快",
        })
        re2 = m_translation_chain.run({
            "source_language": "Chinese",
            "target_language": "Japanese",
            "text": "我喜欢学习大语言模型，轻松简单又愉快",
        })
        print(f're1:\n{re1}')
        print(f're2:\n{re2}')
if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"
    t = TranslatorMultiLanguageOpenAI()
    t.chat()
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
import os
class TranslatorTemplateOpenAI:

    def chat(self):
        template = (
            """You are a translation expert, proficient in various languages. \n
            Translates English to Chinese."""
        )
        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        human_template = "{text}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

        chat_prompt_template = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )
        chat_prompt_template.format_prompt(text="I love programming.")
        chat_prompt = chat_prompt_template.format_prompt(text="I love programming.").to_messages()

        client = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        client.openai_api_key = os.getenv("OPENAI_API_KEY")
        translation_result = client(chat_prompt)
        print(translation_result.content)

if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"
    t = TranslatorTemplateOpenAI()
    t.chat()
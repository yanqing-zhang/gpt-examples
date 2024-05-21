from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
import os
class TranslatorLLChain:
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
        client = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        translation_chain = LLMChain(llm=client, prompt=chat_prompt_template)
        chain_result = translation_chain.run({'text': "I love programming."})
        print(chain_result)
        re1 = translation_chain.run({'text': "I love AI and Large Language Model."})
        re2 = translation_chain.run({'text': "[Fruit, Color, Price (USD)] [Apple, Red, 1.20] [Banana, Yellow, 0.50] [Orange, Orange, 0.80] [Strawberry, Red, 2.50] [Blueberry, Blue, 3.00] [Kiwi, Green, 1.00] [Mango, Orange, 1.50] [Grape, Purple, 2.00]"})
        print(f're1:\n{re1}')
        print(f're2:\n{re2}')

if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"
    t = TranslatorLLChain()
    t.chat()
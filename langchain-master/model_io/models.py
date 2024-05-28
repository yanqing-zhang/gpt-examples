from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import (
AIMessage,
HumanMessage,
SystemMessage
)
import os

"""
langchain最大的缺点是api变化，导致开发人员消耗很多时间找能使用的api，
原来可用的api可能随着langchain版本的迭代而废弃了
"""

class Models:
    def model_exercise(self):
        llm = OpenAI(model_name="gpt-3.5-turbo",api_key=os.getenv("OPENAI_API_KEY"), temperature = 0)
        ret = llm("讲10个程序员听得懂的笑话")
        print(f"ret:\n{ret}")

class ChatModels:

    def chat_model_exercise(self):
        chat_model = ChatOpenAI(model_name="gpt-3.5-turbo",api_key=os.getenv("OPENAI_API_KEY"), temperature = 0)
        messages = [SystemMessage(content="你是一位得力的助手"),
                    HumanMessage(content="谁赢得了2020年的世界大赛冠军？"),
                    AIMessage(content="洛杉矶道奇队赢得了2020年的世界大赛冠军。"),
                    HumanMessage(content="比赛是在哪里进行的？")]
        print(f"messages:\n{messages}")
        response = chat_model(messages)
        print(f"response:\n{response}")
        ret = response.content
        print(f"ret:\n{ret}")

if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"
    models = Models()
    models.model_exercise()
    print("----------------------------------------")
    chat_model = ChatModels()
    chat_model.chat_model_exercise()
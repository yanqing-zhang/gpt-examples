from langchain.chains import ConversationChain
from langchain_community.llms import OpenAI
from langchain.memory import ConversationBufferMemory,ConversationBufferWindowMemory
import os

class MemoryChains:

    def memory_conversation(self):
        llm = OpenAI(model_name="gpt-3.5-turbo-instruct",
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0.75,
            max_tokens=500)
        conversation = ConversationChain(
            llm=llm,
            verbose=True,
            memory=ConversationBufferMemory()
        )
        ret = conversation.predict(input="你好!")
        print(f"ret:\n{ret}")
        print("--------------------------")
        ret2 = conversation.predict(input="你为什么叫小米？跟雷军有关系吗？")
        print(f"ret2:\n{ret2}")
        print("--------------------------")
    def conver_buffer_memory(self):
        llm = OpenAI(model_name="gpt-3.5-turbo-instruct",
                     api_key=os.getenv("OPENAI_API_KEY"),
                     temperature=0.75,
                     max_tokens=500)
        conversation_with_summary = ConversationChain(
            llm=llm,
            memory=ConversationBufferWindowMemory(k=2),
            verbose=True
        )
        ret = conversation_with_summary.predict(input="嗨，你最近过得怎么样？")
        print(f"ret:\n{ret}")
        print("--------------------------")
        ret2 = conversation_with_summary.predict(input="你最近学到什么新知识了?")
        print(f"ret2:\n{ret2}")
        print("--------------------------")
        ret3 = conversation_with_summary.predict(input="展开讲讲？")
        print(f"ret3:\n{ret3}")
        print("--------------------------")
        ret4 = conversation_with_summary.predict(input="如果要构建聊天机器人，具体要用什么自然语言处理技术?")
        print(f"ret4:\n{ret4}")
        print("--------------------------")
        conv_dict = conversation_with_summary.__dict__
        print(f"conv_dict:\n{conv_dict}")
        print("--------------------------")
if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"
    m = MemoryChains()
    if False:
        m.memory_conversation()
    else:
        m.conver_buffer_memory()

from langchain.chains import ConversationChain
from langchain_community.llms import OpenAI
from langchain.memory import ConversationBufferMemory
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
if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"
    m = MemoryChains()
    if False:
        pass
    else:
        m.memory_conversation()
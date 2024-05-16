import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
class ChatModelOpenAI:
    """
    本示例通过langchain调用openai模型实现基本的对话功能
    """
    def chat(self):
        """
        从大模型返回数据为：
        content='2020年世界大赛在美国的德州州阿灵顿的环球生活球场进行。'
        response_metadata={'token_usage':
            {
                'completion_tokens': 32,
                'prompt_tokens': 86,
                'total_tokens': 118
            },
            'model_name': 'gpt-3.5-turbo',
            'system_fingerprint': None,
            'finish_reason': 'stop',
            'logprobs': None
            }
        id='run-e801fd80-7265-4420-b403-13b97a38d78f-0'
        :return:
        """
        message = [SystemMessage(content="你是一位很有用的助手。"),
                   HumanMessage(content="谁赢得了2020年世界大赛?"),
                   AIMessage(content="洛杉矶道奇队赢得2020年世界大赛冠军。"),
                   HumanMessage(content="在哪里进行的比赛?")]
        client = ChatOpenAI(model_name="gpt-3.5-turbo")
        client.openai_api_key = os.getenv("OPENAI_API_KEY")
        client.temperature = 0
        re = client(message)
        print(f're:\n{re}')
        return re

if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"
    c = ChatModelOpenAI()
    re = c.chat()
    content = re.content
    print(f'content:\n{content}')
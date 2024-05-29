from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
import os

class Prompts:
    """
    把prompt当函数一样构造，当函数一样使用
    """
    def from_prompts(self):
        prompt_template = PromptTemplate.from_template("Tell me a {adjective} joke about {content}.")
        prompt = prompt_template.format(adjective="funny",content="chickens")
        print(f"prompt:\n{prompt}")
        print(f"prompt_template:\n{prompt_template}")

    def construct_prompts(self):
        """
        结果：
        valid_prompt:
        input_variables=['adjective', 'content'] template='Tell me a {adjective} joke about {content}.'
        prompt:
        Tell me a funny joke about chickens.
        :return:
        """
        valid_prompt = PromptTemplate(
            input_variables = ["adjective", "content"],
            template = "Tell me a {adjective} joke about {content}."
        )
        prompt = valid_prompt.format(adjective="funny",content="chickens")
        print(f"valid_prompt:\n{valid_prompt}")
        print(f"prompt:\n{prompt}")


    def openai_prompts(self):
        """
        结果：
        1. 为什么程序员喜欢用黑色背景的编辑器？
        因为黑色背景可以减少眼睛的疲劳，让他们可以更专注地写代码，而不是被花花绿绿的颜色分散注意力。

        2. 有一个程序员和一个设计师一起去旅行，路上遇到了一只羊。
        程序员说：“这是一只白色的羊。”
        设计师却说：“不，这是一只白色的羊，但是它的毛色是#FFFFFF。”
        :return:
        """
        p_template = PromptTemplate.from_template(
            "讲{num}个给程序员听的懂的笑话。"
        )
        llm = OpenAI(model_name="gpt-3.5-turbo-instruct",api_key=os.getenv("OPENAI_API_KEY"), temperature = 0)
        prompt = p_template.format(num=2)
        print(f"prompt:\n{prompt}")
        print("========================")
        response = llm(prompt)
        print(f"response:\n{response}")

    def jinja2_prompt(self):
        """
        需要提前安装jinja2
        pip install jinja2 -i https://pypi.tuna.tsinghua.edu.cn/simple
        :return:
        """
        jinja2_template = "Tell me a {{ adjective }} joke about {{ content }}"
        prompt = PromptTemplate.from_template(jinja2_template,template_format="jinja2")

        p = prompt.format(adjective="funny", content="chickens")
        print(f"prompt:\n{prompt}")
        print(f"p:\n{p}")

    def sort_prompt(self):
        prompt_template = PromptTemplate.from_template("生成可执行的快速排序{programming_language}代码")
        prompt_python = prompt_template.format(programming_language="python")
        llm = OpenAI(model_name="gpt-3.5-turbo-instruct", api_key=os.getenv("OPENAI_API_KEY"), temperature=0)
        ret_py = llm(prompt_python)
        print(f"python-ret:\n{ret_py}")
        print("-------------------------------")
        prompt_java = prompt_template.format(programming_language="java")
        ret_java = llm(prompt_java)
        print(f"java-ret:\n{ret_java}")

    def chat_prompt(self):
        template = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful AI bot. Your name is {name}."),
            ("human", "Hello, how are you doing?"),
            ("ai", "I'm doing well, thanks!"),
            ("human", "{user_input}"),
        ])
        message = template.format_messages(
            name = "Bob",
            user_input = "What is your name?"
        )
        print(f"message[0]:\n{message[0].content}")
        print(f"message[-1]:\n{message[-1].content}")
        chat_model = ChatOpenAI(model_name="gpt-3.5-turbo", max_tokens=1000)
        ret = chat_model(message)
        print(f"ret:\n{ret}")
        print("===============================")
        print(f"ret.content:\n{ret.content}")

if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"
    p = Prompts()
    if False:
        p.from_prompts()
        print("-----------------------------")
        p.construct_prompts()
        print("################################")
        p.openai_prompts()
        p.jinja2_prompt()
        p.sort_prompt()
    else:
        p.chat_prompt()
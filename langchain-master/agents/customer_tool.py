from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.agents import OpenAIFunctionsAgent
from langchain.agents import AgentExecutor
from langchain.agents import tool
import os
import pandas as pd

"""
自定义tools,从而实现用户自己的业务
"""
class CustomTool:

    @tool
    def get_word_length(word: str) -> int:
        """Returns the length of a word."""
        return len(word)

    def c_tools(self):
        llm = ChatOpenAI(model_name="gpt-3.5-turbo",
                         api_key=os.getenv("OPENAI_API_KEY"),
                         temperature = 0)
        tools = [self.get_word_length]
        system_messages = SystemMessage(content="你是非常强大的AI助手，但在计算单词长度方面不擅长。")
        prompt = OpenAIFunctionsAgent.create_prompt(system_message=system_messages)
        agent = OpenAIFunctionsAgent(
            llm=llm,
            tools=tools,
            prompt=prompt
        )
        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
        ret = agent_executor.run("单词#student#中有多少个字母?")
        print("-------------------")
        print(f"ret:\n{ret}")

    @tool
    def get_student_info(student_name:str):
        """Returns the information of a student."""
        print(f"#######student_name:{student_name}")
        df = pd.read_excel("../datas/students.xlsx",sheet_name="Sheet1")
        student_info = df.query(f"姓名 == '{student_name}'")
        return student_info

    @tool
    def get_max_score_stu_info(*args):
        """返回各科成绩总和最高的学生信息."""
        df = pd.read_excel("../datas/students.xlsx", sheet_name="Sheet1")
        df['总成绩'] = df[['语文', '数学', '英语', '化学', '物理']].sum(axis=1)
        max_score_index = df['总成绩'].idxmax()
        top_student_info = df.loc[max_score_index]
        return top_student_info

    def stu_tool_agent(self):
        llm = ChatOpenAI(model_name="gpt-3.5-turbo",
                         api_key=os.getenv("OPENAI_API_KEY"),
                         temperature=0)
        tools = [self.get_student_info, self.get_max_score_stu_info]
        system_messages = SystemMessage(content="你是非常强大的AI助手，但在具体业务方面确实不善长，如学生信息查询。")
        prompt = OpenAIFunctionsAgent.create_prompt(system_message=system_messages)
        agent = OpenAIFunctionsAgent(
            llm=llm,
            tools=tools,
            prompt=prompt
        )
        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
        ret = agent_executor.run("查询姓名为#李四#这个学生的信息")
        print("-------------------")
        print(f"ret:\n{ret}")
        average_score = agent_executor.run("把学生#李四#的各科成绩求平均分")
        print(f"average_score:\n{average_score}")
        print("-------------------")
        max_score = agent_executor.run("获取各科成绩总和最高的学生信息")
        print(f"max_score:\n{max_score}")

if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"
    c = CustomTool()
    if False:
        c.c_tools()
    else:
        c.stu_tool_agent()
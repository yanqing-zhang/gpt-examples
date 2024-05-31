from langchain.output_parsers import CommaSeparatedListOutputParser,DatetimeOutputParser
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
import os

class Outputs:
    """
    对输出的纯文本进行更结构化处理
    """
    def out_parser(self):
        # 创建一个输出解析器，用于处理带逗号分隔的列表输出
        output_parser = CommaSeparatedListOutputParser()
        # 获取格式化指令，该指令告诉模型如何格式化其输出
        format_instructions = output_parser.get_format_instructions()

        prompt = PromptTemplate(
            template="List five {subject}.\n{format_instructions}",  # 模板内容
            input_variables=["subject"],  # 输入变量
            partial_variables={"format_instructions": format_instructions}  # 预定义的变量，这里我们传入格式化指令
        )
        _input = prompt.format(subject="ice cream flavors")
        print(f"_input:\n{_input}")
        print("-------------------------------")
        llm = OpenAI(model_name="gpt-3.5-turbo-instruct",api_key=os.getenv("OPENAI_API_KEY"), temperature = 0)
        output = llm(_input)
        print(f"output:\n{output}")
        print("-------------------------------")
        ret = output_parser.parse(output)
        print(f"ret:\n{ret}")
    def out_date_parser(self):
        output_parser = DatetimeOutputParser()
        template = """Answer the users question:
        {question}
        {format_instructions}"""
        prompt = PromptTemplate.from_template(
            template,
            partial_variables={"format_instructions":output_parser.get_format_instructions()}
        )
        print(f"prompt:\n{prompt}")
        print("----------------------------")
        f = prompt.format(question="around when was bitcoin founded?")
        print(f"f:\n{f}")
        llm = OpenAI(model_name="gpt-3.5-turbo-instruct",api_key=os.getenv("OPENAI_API_KEY"), temperature = 0)
        chain = LLMChain(prompt=prompt,llm=llm)
        out = chain.run("around when was bitcoin founded?")
        print("--------------------")
        print(f"out:\n{out}")
        print("--------------------")
        ds = output_parser.parse(out)
        print(f"ds:\n{ds}")

if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"
    o = Outputs()
    if False:
        o.out_parser()
    else:
        o.out_date_parser()
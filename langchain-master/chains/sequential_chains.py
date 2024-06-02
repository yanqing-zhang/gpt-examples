import os
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
class SequentialChians:

    def llmchains(self):
        llm = OpenAI(model_name="gpt-3.5-turbo-instruct",
                     api_key=os.getenv("OPENAI_API_KEY"),
                     temperature = 0.75,
                     max_tokens=500)
        prompt = PromptTemplate(
            input_variables=["product"],
            template="给制造{product}的有限公司取10个好名字，并给出完整的公司名称",
        )
        chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
        ret = chain.run({'product': "性能卓越的GPU"})
        print(f"ret:\n{ret}")


if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"

    s = SequentialChians()
    s.llmchains()
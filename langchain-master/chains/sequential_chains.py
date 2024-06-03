import os
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain,SimpleSequentialChain,SequentialChain
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

    def simple_sque_chain(self):
        llm = OpenAI(model_name="gpt-3.5-turbo-instruct",
                     api_key=os.getenv("OPENAI_API_KEY"),
                     temperature=0.75,
                     max_tokens=500)
        template = """你是一位剧作家。根据戏剧的标题，你的任务是为该标题写一个简介。
        
        标题：{title}
        剧作家：以下是对上述戏剧的简介："""
        prompt_template = PromptTemplate(input_variables=["title"],
                                         template=template)
        synopsis_chain = LLMChain(llm=llm, prompt=prompt_template)
        template = """你是《纽约时报》的戏剧评论家。根据剧情简介，你的工作是为该剧撰写一篇评论。

        剧情简介：
        {synopsis}
        
        以下是来自《纽约时报》戏剧评论家对上述剧目的评论："""
        prompt_template = PromptTemplate(input_variables=["synopsis"],
                                         template=template)
        review_chain = LLMChain(llm=llm, prompt=prompt_template)
        all_chian = SimpleSequentialChain(chains=[synopsis_chain, review_chain], verbose=True)
        review = all_chian.run("三体人不是无法战胜的")
        print(f"review:\n{review}")
        print("------------------")
        review2 = all_chian.run("星球大战第九季")
        print(f"review2:\n{review2}")
    def multi_input_output_squen_chain(self):
        llm = OpenAI(model_name="gpt-3.5-turbo-instruct",
                     api_key=os.getenv("OPENAI_API_KEY"),
                     temperature=0.75,
                     max_tokens=500)
        template = """你是一位剧作家。根据戏剧的标题和设定的时代，你的任务是为该标题写一个简介。

        标题：{title}
        时代：{era}
        剧作家：以下是对上述戏剧的简介："""
        prompt_template = PromptTemplate(input_variables=["title", "era"],
                                         template=template)
        synopsis_chain = LLMChain(llm=llm,
                                  prompt=prompt_template,
                                  output_key="synopsis",
                                  verbose=True)
        template = """你是《纽约时报》的戏剧评论家。根据该剧的剧情简介，你需要撰写一篇关于该剧的评论。

        剧情简介：
        {synopsis}

        来自《纽约时报》戏剧评论家对上述剧目的评价："""
        prompt_template = PromptTemplate(input_variables=["synopsis"],
                                         template=template)
        review_chain = LLMChain(llm=llm,
                                prompt=prompt_template,
                                output_key="review",
                                verbose=True)
        seque_chain = SequentialChain(chains=[synopsis_chain, review_chain],
                                      input_variables=["era","title"],
                                      output_variables=["synopsis", "review"],
                                      verbose=True)
        ret = seque_chain({"title":"三体人不是无法战胜的", "era": "二十一世纪的新中国"})
        print(f"ret:\n{ret}")
        print(f"synopsis:\n{ret['synopsis']}")
        print(f"review:\n{ret['review']}")

if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"

    s = SequentialChians()
    if False:
        s.llmchains()
        s.simple_sque_chain()
    else:
        s.multi_input_output_squen_chain()
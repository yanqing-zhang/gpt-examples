from langchain.chains.router import MultiRouteChain
from langchain_community.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain.chains.router.llm_router import LLMRouterChain,RouterOutputParser
from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE
from langchain.chains.router import MultiPromptChain
import os

class RouteChains:
    def conversations_chain(self):
        physics_template = """你是一位非常聪明的物理教授。
        你擅长以简洁易懂的方式回答关于物理的问题。
        当你不知道某个问题的答案时，你会坦诚承认。

        这是一个问题：
        {input}"""

        math_template = """你是一位很棒的数学家。你擅长回答数学问题。
        之所以如此出色，是因为你能够将难题分解成各个组成部分，
        先回答这些组成部分，然后再将它们整合起来回答更广泛的问题。

        这是一个问题：
        {input}"""
        prompt_infos = [
            {
                "name": "物理",
                "description": "适用于回答物理问题",
                "prompt_template": physics_template,
            },{
                "name": "数学",
                "description": "适用于回答数学问题",
                "prompt_template": math_template,
            },
        ]
        llm = OpenAI(
            model_name="gpt-3.5-turbo-instruct",
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0.75,
            max_tokens=500)
        destination_chains = {}
        for p_info in prompt_infos:
            name = p_info["name"]
            prompt_template = p_info["prompt_template"]
            prompt = PromptTemplate(template=prompt_template, input_variables=["input"])
            chain = LLMChain(llm=llm, prompt=prompt)
            destination_chains[name] = chain
        default_chain = ConversationChain(llm=llm, output_key="text")
        print(f"type:\n{type(default_chain)}")
        print("---------------------------")
        destinations = [f"{p['name']}:{p['description']}" for p in prompt_infos]
        destinations_str = "\n".join(destinations)
        router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(destinations=destinations_str)
        router_prompt = PromptTemplate(
            template=router_template,
            input_variables=["input"],
            output_parser=RouterOutputParser(),
        )
        router_chain = LLMRouterChain.from_llm(llm, router_prompt)
        print("-----------------------------------")
        print(f"destinations:\n{destinations}")
        print("-----------------------------------")
        print(f"destinations_str:\n{destinations_str}")
        print("-----------------------------------")
        print(f"MULTI_PROMPT_ROUTER_TEMPLATE:\n{MULTI_PROMPT_ROUTER_TEMPLATE}")
        print("-----------------------------------")
        print(f"router_template:\n{router_template}")
        print("-----------------------------------")
        chain = MultiPromptChain(
            router_chain=router_chain,
            destination_chains=destination_chains,
            default_chain=default_chain,
            verbose=True,
        )
        ret1 = chain.run("黑体辐射是什么？?")
        print(f"ret1:\n{ret1}")
        print("-----------------------------------")
        ret2 = chain.run("大于40的第一个质数是多少，使得这个质数加一能被3整除？")
        print(f"ret2:\n{ret2}")
        print("-----------------------------------")
        ret3 = chain.run("黑洞是什么？")
        print(f"ret3:\n{ret3}")
        print("-----------------------------------")
if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"
    r = RouteChains()
    if False:
        pass
    else:
        r.conversations_chain()
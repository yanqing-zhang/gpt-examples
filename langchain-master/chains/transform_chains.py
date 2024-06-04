# -*- coding: utf-8 -*-
import os
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain,SimpleSequentialChain,SequentialChain,TransformChain

class TransformChains:

    def transform_func(self, inputs: dict) -> dict:
        text = inputs["text"]
        # 使用split方法将文本按照"\n\n"分隔为多个段落，并只取前三个，然后再使用"\n\n"将其连接起来。
        shortened_text = "\n\n".join(text.split("\n\n")[:3])
        # 返回裁剪后的文本，用"output_text"作为键。
        return {"output_text": shortened_text}


    def tran_chain(self):
        with open("../datas/the_old_man_and_the_sea.txt", "r", encoding='utf-8') as f:
            novel_text = f.read()
        print(f"novel_text:\n{novel_text}")
        print(f"len:\n{len(novel_text)}")
        print("---------------------------------")
        transform_chain = TransformChain(
            input_variables=["text"],
            output_variables=["output_text"],
            transform=self.transform_func
        )

        transform_novel = transform_chain(novel_text)
        ret = transform_novel["text"]
        print(f"ret:\n{ret}")
        print("-----------------------")
        o_text = transform_novel["output_text"]
        print(f"o_text:\n{o_text}")
        template = """总结下面文本:
        
        {output_text}
        
        总结:"""
        prompt = PromptTemplate(input_variables=["output_text"], template=template)
        llm = OpenAI(model_name="gpt-3.5-turbo-instruct",
                     api_key=os.getenv("OPENAI_API_KEY"),
                     temperature = 0.75,
                     max_tokens=500)
        llm_chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
        response = llm_chain(transform_novel["output_text"][:1000])
        print("----------------------------------")
        print(f"response:\n{response}")
        print("-------------------------------------")
        sequential_chain = SimpleSequentialChain(chains=[transform_chain, llm_chain])
        ret = sequential_chain.run(novel_text[:1000])
        print(f"ret:\n{ret}")
if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"
    tc = TransformChains()
    tc.tran_chain()
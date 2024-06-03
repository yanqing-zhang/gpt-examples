# -*- coding: utf-8 -*-
import os
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain,SimpleSequentialChain,SequentialChain,TransformChain

class TransformChains:

    def transform_func(inputs: dict) -> dict:
        text = input["text"]
        short_text = "\n\n".join(text.split("\n\n")[:3])
        return {"output_text":short_text}

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

if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"
    tc = TransformChains()
    tc.tran_chain()
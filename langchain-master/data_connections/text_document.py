# -*- coding: utf-8 -*-
from langchain_community.embeddings import OpenAIEmbeddings
import os
class CustomTextDocument:

    def query(self):
        embeddings_model = OpenAIEmbeddings()
        embeddings = embeddings_model.embed_documents(
            [
                "Hi there!",
                "Oh, hello!",
                "What's your name?",
                "My friends call me World",
                "Hello World!"
            ]
        )
        ret = embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
        print(f"ret:\n{ret}")

if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"
    c = CustomTextDocument()
    c.query()
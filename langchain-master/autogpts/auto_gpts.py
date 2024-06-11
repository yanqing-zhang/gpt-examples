import os
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import Tool
from langchain_community.tools import WriteFileTool
from langchain_community.tools import ReadFileTool
from langchain_community.embeddings import OpenAIEmbeddings
import faiss
from langchain_community.vectorstores import FAISS
from langchain_community.docstore import InMemoryDocstore
from langchain_experimental.autonomous_agents import AutoGPT
from langchain_community.chat_models import ChatOpenAI

class CustomAutoGPTs:

    def chat(self):
        serp_api_key = os.environ['SERP_API_KEY']
        search = SerpAPIWrapper(serpapi_api_key=serp_api_key)
        tools = [
            Tool(
                name="search",
                func=search.run,
                description="useful for when you need to answer questions about current events. You should ask targeted questions",
            ),
            WriteFileTool(),
            ReadFileTool(),
        ]
        embeddings_model = OpenAIEmbeddings()
        embedding_size = 1536
        index = faiss.IndexFlatL2(embedding_size)
        vectorstore = FAISS(embeddings_model.embed_query, index,InMemoryDocstore({}), {})
        llm = ChatOpenAI(model_name="gpt-4",
                     api_key=os.getenv("OPENAI_API_KEY"),
                     temperature=0,
                     verbose=True)
        agent = AutoGPT.from_llm_and_tools(
            ai_name="Jarvis",
            ai_role="Assistant",
            tools=tools,
            llm=llm,
            memory=vectorstore.as_retriever(
                search_type="similarity_score_threshold",
                search_kwargs={"score_threshold": 0.8}
            ),
        )
        agent.chain.verbose=True
        ret = agent.run(["2023年成都大运会，中国金牌数是多少"])
        print(f"ret:\n{ret}")

if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"
    c = CustomAutoGPTs()
    if False:
        pass
    else:
        c.chat()
import os
from langchain.utilities import SerpAPIWrapper
from langchain_community.llms import OpenAI
from langchain.agents import initialize_agent, AgentType, Tool
class SerpSearchAgents:
    def search(self):
        serp_api_key = os.environ['SERP_API_KEY']
        llm = OpenAI(model_name="gpt-3.5-turbo-instruct",
                             api_key=os.getenv("OPENAI_API_KEY"),
                             temperature = 0.75,
                             max_tokens=500)
        search = SerpAPIWrapper(serpapi_api_key=serp_api_key)
        tools = [
            Tool(
                name="Intermediate Answer",
                func=search.run,
                description="useful for when you need to ask with search",
            )
        ]
        self_ask_with_serp = initialize_agent(
            tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose = True
        )
        ret = self_ask_with_serp.run("第79届联大主席是谁？")
        print(f"ret:\n{ret}")

if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"
    s = SerpSearchAgents()
    s.search()

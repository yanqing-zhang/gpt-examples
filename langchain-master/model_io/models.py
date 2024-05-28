from langchain_community.llms import OpenAI
import os
class Models:

    def model_exercise(self):
        llm = OpenAI(model_name="gpt-3.5-turbo",api_key=os.getenv("OPENAI_API_KEY"), temperature = 0)
        ret = llm("讲10个程序员听得懂的笑话")
        print(f"ret:\n{ret}")


if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"
    models = Models()
    models.model_exercise()
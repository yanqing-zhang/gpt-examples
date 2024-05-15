import requests
import os
from termcolor import colored
GPT_MODEL = "gpt-3.5-turbo"

class Chat:

    def chat_completion_requestx(self, messages=None, functions=None, function_call=None, model=GPT_MODEL):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + os.getenv("OPENAI_API_KEY"),
        }
        json_data = {"model": model, "messages": messages}
        if functions is not None:
            json_data.update({"functions": functions})
        if function_call is not None:
            json_data.update({"function_call": function_call})
        try:
            print(f'json_data:\n{json_data}')
            print(f'headers:\n{headers}')
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=json_data,
            )
            return response
        except Exception as e:
            print("Unable to generate ChatCompletion response")
            print(f"Exception: {e}")
            return e

    def pretty_print_conversation(self, messages):
        """
        定义一个函数pretty_print_conversation，用于打印消息对话内容
        :return:
        """
        role_to_color = {
            "system": "red",
            "user": "green",
            "assistant": "blue",
            "function": "magenta",
        }
        for message in messages:
            if message["role"] == "system":
                print(colored(f"system: {message['content']}\n", role_to_color[message["role"]]))
            elif message["role"] == "user":
                print(colored(f"user: {message['content']}\n", role_to_color[message["role"]]))
            elif message["role"] == "assistant" and message.get("function_call"):
                print(colored(f"assistant[function_call]: {message['function_call']}\n", role_to_color[message["role"]]))
            elif message["role"] == "assistant" and not message.get("function_call"):
                print(colored(f"assistant[content]: {message['content']}\n", role_to_color[message["role"]]))
            elif message["role"] == "function":
                print(colored(f"function ({message['name']}): {message['content']}\n", role_to_color[message["role"]]))

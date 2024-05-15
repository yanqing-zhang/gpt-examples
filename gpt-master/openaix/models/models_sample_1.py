import os
from openai import OpenAI
from pprint import pprint
class ModelApi:

    def print_model_info(self):
        client = OpenAI()
        # print(OpenAI.__file__)
        models = client.models.list()
        print(f"models:{models}")
        datas = models.data
        id = models.data[0].id
        print(f'id:{id}')
        model_list = [model.id for model in models.data]
        print(f'model_list:\n{model_list}')

        gpt_3 = client.models.retrieve("text-davinci-003")
        print(f'gpt_3:{gpt_3}')
        gpt_4 = client.models.retrieve("gpt-4-vision-preview")
        print(f'gpt_4:{gpt_4}')

    def completion_api_generate_en_text(self):
        """
        data:
        Completion(id='cmpl-9NzlTgOLnT0OnXEZ3y1L9wtwyIa0r', choices=[CompletionChoice(finish_reason='stop', index=0, logprobs=None, text='\n\nThis is a test.')], created=1715505995, model='gpt-3.5-turbo-instruct', object='text_completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=6, prompt_tokens=5, total_tokens=11))
        """
        client = OpenAI()
        data = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt="Say this is a test",
            max_tokens=7,
            temperature=0
        )
        print(f'data:\n{data}')
        text = data.choices[0].text
        print(f'text:{text}')

    def completion_api_generate_cn_text(self):
        """
        使用 Completions API 实现各类文本生成任务
        主要请求参数说明：
        model （string，必填）
        要使用的模型的 ID。可以参考 模型端点兼容性表。
        prompt （string or array，必填，Defaults to ）
        生成补全的提示，编码为字符串、字符串数组、token数组或token数组数组。
        注意，这是模型在训练过程中看到的文档分隔符，所以如果没有指定提示符，模型将像从新文档的开头一样生成。
        stream （boolean，选填，默认 false）
        当它设置为 true 时，API 会以 SSE（ Server Side Event ）方式返回内容，即会不断地输出内容直到完成响应，流通过 data: [DONE] 消息终止。
        max_tokens （integer，选填，默认是 16）
        补全时要生成的最大 token 数。
        提示 max_tokens 的 token 计数不能超过模型的上下文长度。大多数模型的上下文长度为 2048 个token（最新模型除外，它支持 4096）
        temperature （number，选填，默认是1）
        使用哪个采样温度，在 0和2之间。
        较高的值，如0.8会使输出更随机，而较低的值，如0.2会使其更加集中和确定性。
        通常建议修改这个（temperature ）或 top_p 但两者不能同时存在，二选一。
        n （integer，选填，默认为 1）
        每个 prompt 生成的补全次数。
        注意：由于此参数会生成许多补全，因此它会快速消耗token配额。小心使用，并确保对 max_tokens 和 stop 进行合理的设置。
        """
        client = OpenAI()
        data = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt="讲10个给程序员听的笑话",
            max_tokens=1000,
            temperature=0.5
        )
        print(f'data:\n{data}')
        text = data.choices[0].text
        print(f'text:{text}')

    def completion_api_generate_py_codes(self):
        client = OpenAI()
        data = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt="生成可执行的快速排序 Python 代码",
            max_tokens=1000,
            temperature=0
        )
        print(f'data:\n{data}')
        text = data.choices[0].text
        print(f'text:{text}')

    def chat_completion_model_api(self):
        client = OpenAI()
        messages = [
            {
                "role": "user",
                "content": "Hello!"
            }
        ]
        data = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        print(f'data:\n{data}')
        new_message = data.choices[0].message
        print(f'new_message:\n{new_message}')
        messages.append(new_message)
        print(f'messages:\n{messages}')
        print(f'type(new_message):\n{type(new_message)}')
        role = new_message.role
        print(f'role:\n{role}')
        content = new_message.content
        print(f'content:\n{content}')
        messages.pop()
        print(f'messages after pop():\n{messages}')

    def openai_object_to_dict(self):
        client = OpenAI()
        messages = [
            {
                "role": "user",
                "content": "Hello!"
            }
        ]
        data = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        new_message = data.choices[0].message
        new_message_dict = {"role": new_message.role, "content": new_message.content}
        print(f'type of new_message_dict:\n{type(new_message_dict)}')
        messages.append(new_message_dict)
        print(f'messages:\n{messages}')
        new_chat = {
            "role": "user",
            "content": "1.讲一个程序员才听得懂的冷笑话；2.今天是几号？3.明天星期几？"
        }
        messages.append(new_chat)
        pprint(f'messages:\n{messages}')
        data = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        new_message = data.choices[0].message
        print(f'new_message:{new_message}')
        print(f'content of new_message:{new_message.content}')

    def chat_completion_multi_roles_api(self):
        """
        本例把上一次的输出message加入到下一次的提问中，这样每次与OpenAI对话都会带上上一次的结果，形成了上下文
        message_4:带有上一次的上下文，所以回答中体现的是中国
        1. 2008年夏季奥林匹克运动会中，金牌最多的国家是中国，共获得51枚金牌。
        2. 奖牌最多的国家也是中国，获得100枚奖牌（包括51枚金牌、21枚银牌和28枚铜牌）。
        message_5:没带上一次的上下文，所以回答中体现的是当前GPT认识的信息，而不是针对2008年北京奥运会
        1. 金牌最多的国家是美国。
        2. 奖牌最多的国家是美国。
        """
        client = OpenAI()
        messages = [
            {"role": "system", "content": "你是一个乐于助人的体育界专家。"},
            {"role": "user", "content": "2008年奥运会是在哪里举行的？"},
        ]
        data = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        message = data.choices[0].message.content
        print(f'message_1:\n{message}')
        messages.append({"role": "assistant", "content": message})
        print(f'message_2:\n{message}')
        messages.append({"role": "user", "content": "1.金牌最多的是哪个国家？2.奖牌最多的是哪个国家？"})
        print(f'message_3:\n{message}')
        data = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        message = data.choices[0].message.content
        print(f'message_4:\n{message}')
        data = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{'role': 'user', 'content': '1.金牌最多的是哪个国家？2.奖牌最多的是哪个国家？'}]
        )
        message = data.choices[0].message.content
        print(f'message_5:\n{message}')

if __name__ == '__main__':
    api = ModelApi()
    api.chat_completion_multi_roles_api()



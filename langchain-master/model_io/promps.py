# -*- coding: utf-8 -*-
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, FewShotPromptTemplate
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
import os

"""
pip install chromadb -i https://pypi.tuna.tsinghua.edu.cn/simple
"""
class Prompts:
    """
    把prompt当函数一样构造，当函数一样使用
    """
    def from_prompts(self):
        prompt_template = PromptTemplate.from_template("Tell me a {adjective} joke about {content}.")
        prompt = prompt_template.format(adjective="funny",content="chickens")
        print(f"prompt:\n{prompt}")
        print(f"prompt_template:\n{prompt_template}")

    def construct_prompts(self):
        """
        结果：
        valid_prompt:
        input_variables=['adjective', 'content'] template='Tell me a {adjective} joke about {content}.'
        prompt:
        Tell me a funny joke about chickens.
        :return:
        """
        valid_prompt = PromptTemplate(
            input_variables = ["adjective", "content"],
            template = "Tell me a {adjective} joke about {content}."
        )
        prompt = valid_prompt.format(adjective="funny",content="chickens")
        print(f"valid_prompt:\n{valid_prompt}")
        print(f"prompt:\n{prompt}")


    def openai_prompts(self):
        """
        结果：
        1. 为什么程序员喜欢用黑色背景的编辑器？
        因为黑色背景可以减少眼睛的疲劳，让他们可以更专注地写代码，而不是被花花绿绿的颜色分散注意力。

        2. 有一个程序员和一个设计师一起去旅行，路上遇到了一只羊。
        程序员说：“这是一只白色的羊。”
        设计师却说：“不，这是一只白色的羊，但是它的毛色是#FFFFFF。”
        :return:
        """
        p_template = PromptTemplate.from_template(
            "讲{num}个给程序员听的懂的笑话。"
        )
        llm = OpenAI(model_name="gpt-3.5-turbo-instruct",api_key=os.getenv("OPENAI_API_KEY"), temperature = 0)
        prompt = p_template.format(num=2)
        print(f"prompt:\n{prompt}")
        print("========================")
        response = llm(prompt)
        print(f"response:\n{response}")

    def jinja2_prompt(self):
        """
        需要提前安装jinja2
        pip install jinja2 -i https://pypi.tuna.tsinghua.edu.cn/simple
        :return:
        """
        jinja2_template = "Tell me a {{ adjective }} joke about {{ content }}"
        prompt = PromptTemplate.from_template(jinja2_template,template_format="jinja2")

        p = prompt.format(adjective="funny", content="chickens")
        print(f"prompt:\n{prompt}")
        print(f"p:\n{p}")

    def sort_prompt(self):
        prompt_template = PromptTemplate.from_template("生成可执行的快速排序{programming_language}代码")
        prompt_python = prompt_template.format(programming_language="python")
        llm = OpenAI(model_name="gpt-3.5-turbo-instruct", api_key=os.getenv("OPENAI_API_KEY"), temperature=0)
        ret_py = llm(prompt_python)
        print(f"python-ret:\n{ret_py}")
        print("-------------------------------")
        prompt_java = prompt_template.format(programming_language="java")
        ret_java = llm(prompt_java)
        print(f"java-ret:\n{ret_java}")

    def chat_prompt(self):
        template = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful AI bot. Your name is {name}."),
            ("human", "Hello, how are you doing?"),
            ("ai", "I'm doing well, thanks!"),
            ("human", "{user_input}"),
        ])
        message = template.format_messages(
            name = "Bob",
            user_input = "What is your name?"
        )
        print(f"message[0]:\n{message[0].content}")
        print(f"message[-1]:\n{message[-1].content}")
        chat_model = ChatOpenAI(model_name="gpt-3.5-turbo", max_tokens=1000)
        ret = chat_model(message)
        print(f"ret:\n{ret}")
        print("===============================")
        print(f"ret.content:\n{ret.content}")

    def summary_prompt(self):
        summary_template = ChatPromptTemplate.from_messages([
            ("system", "你将获得关于同一主题的{num}篇文章（用-----------标签分隔）。首先总结每篇文章的论点。然后指出哪篇文章提出了更好的论点，并解释原因。"),
            ("human", "{user_input}"),
        ])
        messages = summary_template.format_messages(
            num = 3,
            user_input = """1. [PHP是世界上最好的语言]
PHP是世界上最好的情感派编程语言，无需逻辑和算法，只要情绪。它能被蛰伏在冰箱里的PHP大神轻易驾驭，会话结束后的感叹号也能传达对代码的热情。写PHP就像是在做披萨，不需要想那么多，只需把配料全部扔进一个碗，然后放到服务器上，热乎乎出炉的网页就好了。
-----------
2. [Python是世界上最好的语言]
Python是世界上最好的拜金主义者语言。它坚信：美丽就是力量，简洁就是灵魂。Python就像是那个永远在你皱眉的那一刻扔给你言情小说的好友。只有Python，你才能够在两行代码之间感受到飘逸的花香和清新的微风。记住，这世上只有一种语言可以使用空格来领导全世界的进步，那就是Python。
-----------
3. [Java是世界上最好的语言]
Java是世界上最好的德育课编程语言，它始终坚守了严谨、安全的编程信条。Java就像一个严格的老师，他不会对你怀柔，不会让你偷懒，也不会让你走捷径，但他教会你规范和自律。Java就像是那个喝咖啡也算加班费的上司，拥有对邪恶的深度厌恶和对善良的深度拥护。"""
        )
        print(f"content:\n{messages[-1].content}")
        print("------------------------------------")
        chat_model = ChatOpenAI(model_name="gpt-3.5-turbo", max_tokens=1000)
        chat_result = chat_model(messages)
        print(f"chat_result:\n{chat_result}")
        print("==============================================")
        messages = summary_template.format_messages(
            num=2,
            user_input="""1.认为“道可道”中的第一个“道”，指的是道理，如仁义礼智之类；“可道”中的“道”，指言说的意思；“常道”，指恒久存在的“道”。因此，所谓“道可道，非常道”，指的是可以言说的道理，不是恒久存在的“道”，恒久存在的“道”不可言说。如苏辙说：“莫非道也。而可道者不可常，惟不可道，而后可常耳。今夫仁义礼智，此道之可道者也。然而仁不可以为义，而礼不可以为智，可道之不可常如此。……而道常不变，不可道之能常如此。”蒋锡昌说：“此道为世人所习称之道，即今人所谓‘道理’也，第一‘道’字应从是解。《广雅·释诂》二：‘道，说也’，第二‘道’字应从是解。‘常’乃真常不易之义，在文法上为区别词。……第三‘道’字即二十五章‘道法自然’之‘道’，……乃老子学说之总名也”。陈鼓应说：“第一个‘道’字是人们习称之道，即今人所谓‘道理’。第二个‘道’字，是指言说的意思。第三个‘道’字，是老子哲学上的专有名词，在本章它意指构成宇宙的实体与动力。……‘常道’之‘常’，为真常、永恒之意。……可以用言词表达的道，就不是常道”。
-----------
2.认为“道可道”中的第一个“道”，指的是宇宙万物的本原；“可道”中的“道”，指言说的意思；“常道”，指恒久存在的“道”。因此，“道可道，非常道”，指可以言说的“道”，就不是恒久存在的“道”。如张默生说：“‘道’，指宇宙的本体而言。……‘常’，是经常不变的意思。……可以说出来的道，便不是经常不变的道”。董平说：“第一个‘道’字与‘可道’之‘道’，内涵并不相同。第一个‘道’字，是老子所揭示的作为宇宙本根之‘道’；‘可道’之‘道’，则是‘言说’的意思。……这里的大意就是说：凡一切可以言说之‘道’，都不是‘常道’或永恒之‘道’”。汤漳平等说：“第一句中的三个‘道’，第一、三均指形上之‘道’，中间的‘道’作动词，为可言之义。……道可知而可行，但非恒久不变之道”。
--------
3.认为“道可道”中的第一个“道”，指的是宇宙万物的本原；“可道”中的“道”，指言说的意思；“常道”，则指的是平常人所讲之道、常俗之道。因此，“道可道，非常道”，指“道”是可以言说的，但它不是平常人所谓的道或常俗之道。如李荣说：“道者，虚极之理也。夫论虚极之理，不可以有无分其象，不可以上下格其真。……圣人欲坦兹玄路，开以教门，借圆通之名，目虚极之理，以理可名，称之可道。故曰‘吾不知其名，字之曰道’。非常道者，非是人间常俗之道也。人间常俗之道，贵之以礼义，尚之以浮华，丧身以成名，忘己而徇利。”司马光说：“世俗之谈道者，皆曰道体微妙，不可名言。老子以为不然，曰道亦可言道耳，然非常人之所谓道也。……常人之所谓道者，凝滞于物。”裘锡圭说：“到目前为止，可以说，几乎从战国开始，大家都把‘可道’之‘道’……看成老子所否定的，把‘常道’‘常名’看成老子所肯定的。这种看法其实有它不合理的地方，……‘道’是可以说的。《老子》这个《道经》第一章，开宗明义是要讲他的‘道’。第一个‘道’字，理所应当，也是讲他要讲的‘道’：道是可以言说的。……那么这个‘恒’字应该怎么讲？我认为很简单，‘恒’字在古代作定语用，经常是‘平常’‘恒常’的意思。……‘道’是可以言说的，但是我要讲的这个‘道’，不是‘恒道’，它不是一般人所讲的‘道’。"""
        )
        print(f"messages:\n{messages}")
        print("************************************8")
        chat_result = chat_model(messages)
        print(f"content of chat_result:\n{chat_result.content}")
        messages = summary_template.format_messages(
            num=2,
            user_input='''1.认为“道可道”中的第一个“道”，指的是道理，如仁义礼智之类；“可道”中的“道”，指言说的意思；“常道”，指恒久存在的“道”。因此，所谓“道可道，非常道”，指的是可以言说的道理，不是恒久存在的“道”，恒久存在的“道”不可言说。如苏辙说：“莫非道也。而可道者不可常，惟不可道，而后可常耳。今夫仁义礼智，此道之可道者也。然而仁不可以为义，而礼不可以为智，可道之不可常如此。……而道常不变，不可道之能常如此。”蒋锡昌说：“此道为世人所习称之道，即今人所谓‘道理’也，第一‘道’字应从是解。《广雅·释诂》二：‘道，说也’，第二‘道’字应从是解。‘常’乃真常不易之义，在文法上为区别词。……第三‘道’字即二十五章‘道法自然’之‘道’，……乃老子学说之总名也”。陈鼓应说：“第一个‘道’字是人们习称之道，即今人所谓‘道理’。第二个‘道’字，是指言说的意思。第三个‘道’字，是老子哲学上的专有名词，在本章它意指构成宇宙的实体与动力。……‘常道’之‘常’，为真常、永恒之意。……可以用言词表达的道，就不是常道”。
            -----------
            2.认为“道可道”中的第一个“道”，指的是宇宙万物的本原；“可道”中的“道”，指言说的意思；“常道”，指恒久存在的“道”。因此，“道可道，非常道”，指可以言说的“道”，就不是恒久存在的“道”。如张默生说：“‘道’，指宇宙的本体而言。……‘常’，是经常不变的意思。……可以说出来的道，便不是经常不变的道”。董平说：“第一个‘道’字与‘可道’之‘道’，内涵并不相同。第一个‘道’字，是老子所揭示的作为宇宙本根之‘道’；‘可道’之‘道’，则是‘言说’的意思。……这里的大意就是说：凡一切可以言说之‘道’，都不是‘常道’或永恒之‘道’”。汤漳平等说：“第一句中的三个‘道’，第一、三均指形上之‘道’，中间的‘道’作动词，为可言之义。……道可知而可行，但非恒久不变之道”。
            '''
        )
        chat_result = chat_model(messages)
        print(f"content of chat_result:\n{chat_result.content}")
        print("---------------------------------")
    def fewshot_prompts(self):
        examples = [
            {
                "question": "谁活得更久，穆罕默德·阿里还是艾伦·图灵？",
                "answer":
                    """
                    这里需要进一步的问题吗：是的。
                    追问：穆罕默德·阿里去世时多大了？
                    中间答案：穆罕默德·阿里去世时74岁。
                    追问：艾伦·图灵去世时多大了？
                    中间答案：艾伦·图灵去世时41岁。
                    所以最终答案是：穆罕默德·阿里
                    """
            },
            {
                "question": "craigslist的创始人是什么时候出生的？",
                "answer":
                    """
                    这里需要进一步的问题吗：是的。
                    追问：谁是craigslist的创始人？
                    中间答案：Craigslist是由Craig Newmark创办的。
                    追问：Craig Newmark是什么时候出生的？
                    中间答案：Craig Newmark出生于1952年12月6日。
                    所以最终答案是：1952年12月6日
                    """
            },
            {
                "question": "乔治·华盛顿的外祖父是谁？",
                "answer":
                    """
                    这里需要进一步的问题吗：是的。
                    追问：谁是乔治·华盛顿的母亲？
                    中间答案：乔治·华盛顿的母亲是Mary Ball Washington。
                    追问：Mary Ball Washington的父亲是谁？
                    中间答案：Mary Ball Washington的父亲是Joseph Ball。
                    所以最终答案是：Joseph Ball
                    """
            },
            {
                "question": "《大白鲨》和《皇家赌场》的导演是同一个国家的吗？",
                "answer":
                    """
                    这里需要进一步的问题吗：是的。
                    追问：谁是《大白鲨》的导演？
                    中间答案：《大白鲨》的导演是Steven Spielberg。
                    追问：Steven Spielberg来自哪里？
                    中间答案：美国。
                    追问：谁是《皇家赌场》的导演？
                    中间答案：《皇家赌场》的导演是Martin Campbell。
                    追问：Martin Campbell来自哪里？
                    中间答案：新西兰。
                    所以最终答案是：不是
                    """
            }
        ]
        example_prompt = PromptTemplate(
            input_variables = ["question", "answer"],
            template="Question:{question}\n{answer}"
        )
        """**examples[0] 是将examples[0] 字典的键值对（question-answer）解包并传递给format，作为函数参数"""
        message = example_prompt.format(**examples[0])
        print(f"message:\n{message}")
        print(f"example_prompt:\n{example_prompt}")
        message = example_prompt.format(**examples[-1])
        print(f"message:\n{message}")
        few_shot_prompt = FewShotPromptTemplate(
            examples=examples,
            example_prompt=example_prompt,
            suffix="Question:{input}",
            input_variables=["input"]
        )

        print("================================")
        ret = few_shot_prompt.format(input="玛丽·波尔·华盛顿的父亲是谁?")
        print(f"ret:\n{ret}")

    def example_selector_prompt(self):
        example_prompt = PromptTemplate(
            input_variables = ["input", "output"],
            template = "Input:{input}\nOutput:{output}",
        )
        examples = [
            {"input": "happy", "output": "sad"},
            {"input": "tall", "output": "short"},
            {"input": "energetic", "output": "lethargic"},
            {"input": "sunny", "output": "gloomy"},
            {"input": "windy", "output": "calm"},
        ]
        example_selector = SemanticSimilarityExampleSelector.from_examples(
            examples,
            OpenAIEmbeddings(),
            Chroma,
            k=1
        )
        similar_prompt = FewShotPromptTemplate(
            example_selector=example_selector,
            example_prompt=example_prompt,
            prefix="Give the antonym of every input",
            suffix="Input: {adjective}\nOutput:",
            input_variables=["adjective"],
        )
        f1 = similar_prompt.format(adjective="worried")
        print(f"f:\n{f1}")
        print("------------------")
        f2 = similar_prompt.format(adjective="long")
        print(f"f:\n{f2}")
        print("------------------")
        f3 = similar_prompt.format(adjective="rain")
        print(f"f:\n{f3}")
if __name__ == '__main__':
    os.environ["http_proxy"] = "http://127.0.0.1:10794"
    os.environ["https_proxy"] = "http://127.0.0.1:10794"
    p = Prompts()
    if False:
        p.from_prompts()
        print("-----------------------------")
        p.construct_prompts()
        print("################################")
        p.openai_prompts()
        p.jinja2_prompt()
        p.sort_prompt()
        p.chat_prompt()
        p.summary_prompt()
        p.fewshot_prompts()
    else:
        p.example_selector_prompt()
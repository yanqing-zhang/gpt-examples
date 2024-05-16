from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate
)
class ChatTemplateModelOpenAI:

    def chat(self):
        template = (
            """You are a translation expert, proficient in various languages. \n
               Translates English to Chinese."""
        )
        system_message_prompt = SystemMessagePromptTemplate.format_messages(template)
        print(f'system_message_prompt:\n{system_message_prompt}')
        human_template = "{text}"
        human_message_prompt = HumanMessagePromptTemplate.format_messages(human_template)
        print(f'human_message_prompt:\n{human_message_prompt}')
        chat_prompt_template = ChatPromptTemplate.format_messages(
            [system_message_prompt, human_message_prompt]
        )
        print(f'chat_prompt_template:\n{chat_prompt_template}')
        chat_prompt_template.format_prompt(text="I love programming.")
        chat_prompt = chat_prompt_template.format_prompt(text="I love programming.").to_messages()
        print(f'chat_prompt:\n{chat_prompt}')
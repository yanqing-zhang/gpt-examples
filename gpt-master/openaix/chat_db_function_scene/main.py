from openai.chat_db_function_scene.messages_a_scene import MessagesAscene
from openai.chat_db_function_scene.messages_b_scene import MessagesBscene

def process(scene_num:str):
    messages = None
    if scene_num == 'a':
        messages = MessagesAscene()
    if scene_num == 'b':
        messages = MessagesBscene()
    if messages is not None:
        messages.do_message()

if __name__ == '__main__':
    process("b") # a,b
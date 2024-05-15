from openaix.chat_function_scene.chat_f import Chat
from openaix.chat_function_scene.function_calls import Functions
from openaix.chat_function_scene.messages_a_scene import MessagesAscene
from openaix.chat_function_scene.messages_b_scene import MessagesBscene
from openaix.chat_function_scene.messages_c_scene import MessagesCscene
from openaix.chat_function_scene.messages_d_scene import MessagesDscene
from openaix.chat_function_scene.messages_e_scene import MessagesEscene
from openaix.chat_function_scene.messages_f_scene import MessagesFscene
from openaix.chat_function_scene.messages_g_scene import MessagesGscene

def get_messages(scene_num:str):
    if scene_num == "a":
        messagex = MessagesAscene()
    if scene_num == "b":
        messagex = MessagesBscene()
    if scene_num == "c":
        messagex = MessagesCscene()
    if scene_num == "d":
        messagex = MessagesDscene()
    if scene_num == "e":
        messagex = MessagesEscene()
    if scene_num == "f":
        messagex = MessagesFscene()
    if scene_num == "g":
        messagex = MessagesGscene()
    return messagex

def process(scene_num:str):
    """
    入口函数
    :return:
    """
    chat = Chat()
    ff = Functions()

    messagex = get_messages(scene_num)

    chat_response = None
    if scene_num in ["a", "b", "c", "d", "e", "f"]:
        chat_response = chat.chat_completion_requestx(
            messages=messagex, functions=ff.get_functions()
        )
    if scene_num in ["g"]:
        chat_response = chat.chat_completion_requestx(
            messages=messagex, functions=ff.get_functions(), function_call="none"
        )
    assistant_message = chat_response.json()["choices"][0]["message"]
    messagex.append(assistant_message)
    chat.pretty_print_conversation(messagex)

if __name__ == '__main__':
    process("a") # a,b,c,d,e,f,g
from openaix.chat_db_function_scene.chat_f import Chat
from openaix.chat_db_function_scene.openai_functions import Functions
from openaix.chat_db_function_scene.db_info import DbInfo
class MessagesAscene:

    def do_message(self):
        chat = Chat()
        f = Functions()
        db_info = DbInfo()
        database_schema_string = db_info.get_sqlite_db_info()
        messages = []
        messages.append({"role": "system",
                         "content": "Answer user questions by generating SQL queries against the Chinook Music Database."})

        messages.append({"role": "user", "content": "Hi, who are the top 5 artists by number of tracks?"})
        chat_response = chat.chat_completion_request(messages, f.get_functions(database_schema_string))
        assistant_message = chat_response.json()["choices"][0]["message"]
        messages.append(assistant_message)
        if assistant_message.get("function_call"):
            results = f.execute_function_call(assistant_message)
            messages.append(
                {"role": "function", "name": assistant_message["function_call"]["name"], "content": results})
        chat.pretty_print_conversation(messages)
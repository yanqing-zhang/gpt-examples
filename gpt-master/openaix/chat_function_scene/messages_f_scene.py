class MessagesFscene:
    """
    F场景：结果
    system: Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous.
    user: Give me a weather report for San Diego, USA.
    assistant[function_call]: {'name': 'get_current_weather', 'arguments': '{\n  "location": "San Diego, USA",\n  "format": "celsius"\n}'}
    """
    def do_messages(self):
        messages = []
        # step-1 ~------------------------------
        messages.append({
            "role": "system",  # 角色为系统
            "content": "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous."
        })

        # 添加用户角色的消息
        messages.append({
            "role": "user",  # 角色为用户
            "content": "Give me a weather report for San Diego, USA."
        })

        return messages
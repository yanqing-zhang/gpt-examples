class MessagesBscene:
    """
    B场景：结果
    system: Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous.
    user: What's the weather like today
    assistant[content]: Sure, can you please provide me with your location?
    user: I'm in Shanghai, China.
    assistant[function_call]: {'name': 'get_current_weather', 'arguments': '{\n  "location": "Shanghai, China",\n  "format": "celsius"\n}'}
    """
    def do_messages(self):
        messages = []
        # step-1 ~------------------------------
        messages.append({
            "role": "system",
            "content": "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous."
        })
        messages.append({
            "role": "user",
            "content": "What's the weather like today"
        })
        # step-2 ~------------------------------
        messages.append({
            "role": "user",
            "content": "I'm in Shanghai, China."
        })

        return messages
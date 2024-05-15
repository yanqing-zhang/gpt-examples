class MessagesCscene:
    """
    C场景：结果
    system: Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous.
    user: what is the weather going to be like in Shanghai, China over the next x days
    assistant[content]: Sure, I can help you with that. Please provide the number of days you would like the weather forecast for.

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
            "content": "what is the weather going to be like in Shanghai, China over the next x days"
        })

        return messages
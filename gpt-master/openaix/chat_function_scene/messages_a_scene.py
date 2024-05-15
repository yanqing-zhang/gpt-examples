class MessagesAscene:
    """
    A场景：结果
    system: Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous.
    user: What's the weather like today
    assistant[content]: Sure, can you please provide me with your location?
    """
    def do_messages(self):
        messages = []
        messages.append({
            "role": "system",
            "content": "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous."
        })
        messages.append({
            "role": "user",
            "content": "What's the weather like today"
        })

        return messages
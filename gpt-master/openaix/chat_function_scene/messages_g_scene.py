class MessagesGscene:
    """
    G场景：结果
    system: Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous.
    user: Give me the current weather (use Celcius) for Toronto, Canada.
    assistant[content]: {
      "location": "Toronto, Canada",
      "format": "celsius"
    }
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
            "content": "Give me the current weather (use Celcius) for Toronto, Canada."
        })

        return messages
class MemoryService:

    def __init__(self):

        self.conversation = []

    def add_message(self, role, content):

        self.conversation.append(
            {
                "role": role,
                "content": content
            }
        )

    def get_messages(self):

        return self.conversation

    def clear(self):

        self.conversation = []
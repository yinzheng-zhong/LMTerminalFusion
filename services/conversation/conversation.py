from services.conversation.initial_content import INITIAL_CONTENT
from services.conversation.message import user, assistant, user_general


class Conversation:
    def __init__(self):
        self._messages = None
        self._goal = None

        self.reset()

    def set_goal(self, goal):
        self._goal = goal
        self.add_terminal_message("")

    def add_terminal_message(self, message):
        self._messages.append(user(terminal_stdout=message, goal=self._goal))

    def add_lm_message(self, message):
        self._messages.append(assistant(message))

    def get_conversation(self):
        return self._messages

    def hint(self):
        """
        Temporarily swap the last message with a hint message.
        """
        previous_message = self._messages[-1]
        if previous_message['role'] == 'user':
            message_with_hint = (
                    previous_message['content'] +
                    " HINT: You have not provided any shell command. Provide a shell command to write the file."
            )
            return self._messages[:-1] + [user_general(message_with_hint)]

    def reset(self):
        self._messages = INITIAL_CONTENT
        self._goal = ""

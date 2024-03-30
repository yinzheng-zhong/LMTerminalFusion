from services.conversation.message import user, assistant, user_general, system
from services.conversation.initial_content import INITIAL_CONTENT


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

    def add_lm_raw_message(self, message):
        self._messages.append(assistant(message))

    def add_lm_command(self, command):
        self._messages.append(assistant("```shell\n" + command + "\n```"))

    def get_conversation(self):
        return self._messages

    def remove_last_message(self):
        self._messages = self._messages[:-1]

    def emphasise(self):
        """
        Temporarily swap the last message with a hint message.
        """
        previous_message = self._messages[-1]
        if previous_message['role'] == 'assistant':
            message_with_hint = (
                    "HINT: I can't find any shell command above. You should only provide shell commands" +
                    " like ```shell\nls -la\n``` for any operation. " +
                    "If you need to write the code into a file, use ```shell\necho 'your code' > file.py\n```"
            )
            return self._messages + [user_general(message_with_hint)]

    def reset(self):
        self._messages = INITIAL_CONTENT
        self._goal = ""

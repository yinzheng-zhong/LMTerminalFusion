from packages.conversation.initial_content import INITIAL_CONTENT
from packages.conversation.message import user, assistant


class Conversation:
    def __init__(self):
        self.messages = None
        self.goal = None

        self.reset()

    def set_goal(self, goal):
        self.goal = goal
        self.add_terminal_message("")

    def add_terminal_message(self, message):
        self.messages.append(user(terminal_stdout=message, goal=self.goal))

    def add_lm_message(self, message):
        self.messages.append(assistant(message))

    def reset(self):
        self.messages = INITIAL_CONTENT
        self.goal = ""

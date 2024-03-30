import colorama
from services.lm.api import API


class LM:
    def __init__(
            self,
            api: API
    ):
        self.api = api

    def get_lm_reply(self, conversation):
        print(
            colorama.Fore.GREEN + colorama.Style.BRIGHT +
            "Querying the LM" + colorama.Style.RESET_ALL
        )

        return self.api.lm_query(conversation)

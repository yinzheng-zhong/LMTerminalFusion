import os
import logging
import time
from openai import OpenAI
from services.Env.env import EnvironmentValues


class API:
    def __init__(
            self,
            env: EnvironmentValues
    ):
        self.env = env

        self.client = self._get_client()
        self.logger = logging.getLogger()

    def _get_client(self):
        client = OpenAI(
            base_url=os.environ.get("OPENAI_API_BASE"),
            api_key=os.environ.get("OPENAI_API_KEY")
        )

        return client

    def lm_query(
            self,
            message: list,
            max_retries=3,
            sleep_time=2
    ) -> str:
        retries = 0

        while retries < max_retries:
            try:
                completion = self.client.chat.completions.create(
                    model=self.env.get_value("OPENAI_MODEL"),
                    messages=message,
                    temperature=0.3
                )
                reply_content = completion.choices[0].message.content
                if reply_content:
                    return reply_content
            except Exception as e:
                self.logger.warning("Error during gpt_query(): %s", e)
                retries += 1
                time.sleep(sleep_time)

        raise Exception("Maximum retries exceeded. Check your code for errors.")


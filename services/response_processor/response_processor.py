class ResponseProcessor:
    def process(self, response: str) -> str:
        processed = self._extract_command(response)

        return processed

    def _extract_command(self, response: str):
        """
        The extract_command method is used to extract the command from the ```shell\n{command}\n```.
        """
        # if no markup is found, return as it is
        if "```" not in response:
            return response

        # search for ```shell
        start = response.find("```shell")
        if start == -1:
            return None

        # search for ``` after ```shell
        end = response.find("```", start + 7)
        if end == -1:
            return None

        # extract the command
        command = response[start + 8:end]

        # remove \n
        command = command.strip()

        return command

    def find_issue(self, response):
        """
        Figure out what markup it uses other than ```shell
        :param response:
        :return:
        """

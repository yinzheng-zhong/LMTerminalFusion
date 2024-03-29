from packages.terminal.sub_process import SubProcess


class Terminal:
    def __init__(
            self,
            sub_process: SubProcess
    ):
        self.sub_process = sub_process

    def execute_command(self, command: str) -> [str]:
        stdout = self.sub_process.run_process(command)
        return self._format_terminal_output(stdout)

    def _format_terminal_output(self, term_output: [str]) -> [str]:
        if len(term_output) == 0:
            term_output = [""]

        term_output = term_output[-1000:]
        return "\n".join(term_output)

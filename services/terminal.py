import subprocess


class TerminalService:
    """Service class to interact with the terminal."""

    def __init__(self):
        self.process = None

    def execute_command(self, command) -> [str]:
        """Method to execute a command and get the output."""
        self.process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        output = []

        while True:
            stdout = self.process.stdout.readline()
            if stdout == b'':
                break
            else:
                output.append(stdout.strip().decode("UTF-8"))

        while True:
            stderr = self.process.stderr.readline()
            if stderr == b'':
                break
            else:
                output.append(stderr.strip().decode("UTF-8"))

        return output

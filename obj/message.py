def assistant(content: str):
    return {"role": "assistant", "content": content}


def user(terminal_stdout: str, goal: str):
    return {"role": "user", "content": "GOAL: " + goal + "\nTERMINAL STDOUT: " + terminal_stdout}


INSTRUCTION = ('You are an assistant that writes and reads the console commands to achieve the programming goal. ' +
               'Your responses (command) will be one command at a time, with each response JUST the console command and nothing else. ' +
               'The GOAL specifies the goal, TERMINAL STDOUT is the terminal output from your previous command. ' +
               'You receive the last 1000 lines of the terminal output and you then respond with the next command. ' +
               'You have to try to fix the errors based on the terminal output. ' +
               'When we reached the end of console commands, respond "DONE" and then you will do it again with some new GOAL from the user.')


def system():
    return {"role": "system", "content": INSTRUCTION}

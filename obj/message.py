def assistant(content: str):
    return {"role": "assistant", "content": content}


def user(content: str):
    return {"role": "user", "content": content}


INSTRUCTION = ('You are an assistant that writes and reads the console commands to achieve the programming goal. ' +
               'Your responses (command) will be one command at a time, with each response JUST the console command and nothing else. ' +
               'The GOAL specifies the goal, the user start the conversation with "GOAL:", then the user message is the terminal output. ' +
               'You receive the last 1000 lines of the terminal output and you then respond with the next command. ' +
               'You have to try to fix the errors based on the terminal output. ' +
               'When we reached the end of console commands, respond "DONE" and then you will do it again with some new GOAL from the user.')


def system(goal: str):
    return {"role": "system", "content": "INSTRUCTION: " + INSTRUCTION + " GOAL: " + goal}

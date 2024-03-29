def assistant(content: str):
    return {"role": "assistant", "content": content}


def user(terminal_stdout: str, goal: str):
    return {"role": "user", "content": "GOAL: " + goal +
                                       "\nTERMINAL OUTPUT: " + terminal_stdout
            }


INSTRUCTION = 'You are an assistant that controls the terminal to achieve the programming goal. ' + \
              'Your response (command) should be a single console command at a time. Each response should contain just the console command, without any additional text, comments or information. ' + \
              'You receive the last terminal output, from which you should decide and respond with the next console command. ' + \
              'You are required to fix any errors raised based on this terminal output. ' + \
              'If there is no further command to execute (i.e., when we have reached the goal), respond with the message "DONE" and await new instructions.'


def system():
    return {"role": "system", "content": INSTRUCTION}

from services.terminal import TerminalService
from services.lm import api
from obj.initial_content import INITIAL_CONTENT
from obj.message import user, assistant, system
import colorama

# create a Python program to print out Hello World
conversation = INITIAL_CONTENT

term = TerminalService()

while True:
    goal = input("Enter a command: ")
    message = user('GOAL: ' + goal)
    system_message = system(goal)
    conversation = conversation + [message, system_message]
    ini_ml_reply = api.lm_query(conversation)
    print(
        colorama.Fore.CYAN + colorama.Style.BRIGHT + "The LM wants to execute:\n" + ini_ml_reply + colorama.Style.RESET_ALL
    )

    conversation = conversation + [assistant(ini_ml_reply)]

    command = ini_ml_reply

    while True:
        input("Press Enter to confirm execution...")
        term_output = term.execute_command(command)

        if len(term_output) == 0:
            term_output = ["\n"]

        # take the last 10 lines of output
        term_output = term_output[-10:]
        # implode the output list into a string
        term_output = "\n".join(term_output)

        print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "Terminal Output:\n"  + term_output + colorama.Style.RESET_ALL)

        # add the terminal output to the content
        conversation = conversation + [user(term_output), system_message]

        print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "Querying the LM" + colorama.Style.RESET_ALL)

        ml_reply = api.lm_query(conversation)
        print(
            colorama.Fore.CYAN + colorama.Style.BRIGHT + "The LM wants to execute:\n" + ml_reply + colorama.Style.RESET_ALL
        )

        conversation = conversation + [assistant(ml_reply)]

        if 'DONE' in ml_reply:
            print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "Done reached." + colorama.Style.RESET_ALL)
            break

        command = ml_reply

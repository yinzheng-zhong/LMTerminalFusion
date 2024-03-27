from packages.lm import lm
from packages.terminal import terminal
from obj.initial_content import INITIAL_CONTENT
from obj.message import user, assistant
import colorama


def execute_command_with_feedback(command, goal, conversation):
    while True:
        input("Press Enter to confirm execution...")
        term_output = terminal.execute_command(command)
        print_terminal_output(term_output)

        new_conversation = update_conversation(conversation, term_output, goal)
        lm_reply = lm.get_lm_reply(new_conversation)

        print_lm_execution(lm_reply)

        if 'DONE' in lm_reply:
            print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "Done reached." + colorama.Style.RESET_ALL)
            conversation = INITIAL_CONTENT
            break

        command = lm_reply

    return conversation


def print_terminal_output(term_output):
    print(
        colorama.Fore.YELLOW + colorama.Style.BRIGHT +
        "Terminal Output:\n" + term_output + colorama.Style.RESET_ALL
    )


def update_conversation(conversation, term_output, goal):
    return conversation + [user(terminal_stdout=term_output, goal=goal)]


def print_lm_execution(lm_execution):
    print(
        colorama.Fore.CYAN + colorama.Style.BRIGHT +
        "The LM wants to execute:\n" + lm_execution + colorama.Style.RESET_ALL
    )


def main():
    conversation = INITIAL_CONTENT

    while True:
        goal = input("Enter a command: ")
        message = user(terminal_stdout="NEW GOAL", goal=goal)
        conversation = conversation + [message]
        ini_lm_reply = lm.get_lm_reply(conversation)

        print_lm_execution(ini_lm_reply)

        conversation = conversation + [assistant(ini_lm_reply)]

        command = ini_lm_reply
        conversation = execute_command_with_feedback(command, goal, conversation)


if __name__ == '__main__':
    main()

from services.lm import lm
from services.terminal import terminal
import colorama
from services.conversation import conversation
from services.response_processor import response_processor


def print_terminal_output(term_output):
    print(
        colorama.Fore.YELLOW + colorama.Style.BRIGHT +
        "Terminal Output:\n" + term_output + colorama.Style.RESET_ALL
    )


def print_lm_execution(lm_execution):
    print(
        colorama.Fore.CYAN + colorama.Style.BRIGHT +
        "The LM wants to execute:\n" + lm_execution + colorama.Style.RESET_ALL
    )


def main():
    while True:
        goal = input("Enter a command: ")
        conversation.set_goal(goal)

        while True:
            lm_reply = lm.get_lm_reply(conversation.get_conversation())
            if 'DONE' in lm_reply:
                print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "Done reached." + colorama.Style.RESET_ALL)
                conversation.reset()
                break

            lm_reply = response_processor.process(lm_reply)
            if lm_reply is None:
                print(colorama.Fore.RED + colorama.Style.BRIGHT + "LM hasn't return any shell command." + colorama.Style.RESET_ALL)
                lm_reply = conversation.hint()
                lm_reply = lm.get_lm_reply(lm_reply)
                lm_reply = response_processor.process(lm_reply)

            print_lm_execution(lm_reply)
            conversation.add_lm_message(lm_reply)

            input("Press Enter to confirm execution...")
            term_output = terminal.execute_command(lm_reply)
            print_terminal_output(term_output)
            conversation.add_terminal_message(term_output)


if __name__ == '__main__':
    main()

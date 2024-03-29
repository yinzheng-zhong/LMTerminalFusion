from packages.lm import lm
from packages.terminal import terminal
import colorama
from packages.conversation import conversation


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
            lm_reply = lm.get_lm_reply(conversation.messages)
            print_lm_execution(lm_reply)
            conversation.add_lm_message(lm_reply)
            if 'DONE' in lm_reply:
                print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "Done reached." + colorama.Style.RESET_ALL)
                conversation.reset()
                break

            input("Press Enter to confirm execution...")
            term_output = terminal.execute_command(lm_reply)
            print_terminal_output(term_output)
            conversation.add_terminal_message(term_output)


if __name__ == '__main__':
    main()

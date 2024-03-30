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


def retry_for_shell_command():
    """
    Try to ask the LM to return a shell command.
    :return:
    """
    print(
        colorama.Fore.RED + colorama.Style.BRIGHT +
        "LM hasn't return any shell command. Trying to emphasise the requirement" +
        colorama.Style.RESET_ALL
    )
    lm_reply = conversation.emphasise()
    lm_reply = lm.get_lm_reply(lm_reply)
    return response_processor.process(lm_reply)


def main():
    while True:
        goal = input("Enter a command: ")
        conversation.set_goal(goal)

        while True:
            lm_reply_raw = lm.get_lm_reply(conversation.get_conversation())
            if 'DONE' in lm_reply_raw:
                print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "Done reached." + colorama.Style.RESET_ALL)
                conversation.reset()
                break

            command = response_processor.process(lm_reply_raw)
            if command:
                conversation.add_lm_command(command)
            else:
                conversation.add_lm_raw_message(lm_reply_raw)

            while command is None:
                command = retry_for_shell_command()
                if command:
                    # Remove the last wrong message and add the new message as command
                    conversation.remove_last_message()
                    conversation.add_lm_command(command)
                    break

            print_lm_execution(command)

            input("Press Enter to confirm execution...")
            term_output = terminal.execute_command(command)
            print_terminal_output(term_output)
            conversation.add_terminal_message(term_output)


if __name__ == '__main__':
    main()

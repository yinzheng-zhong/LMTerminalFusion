from packages.terminal.sub_process import SubProcess as _SubProcess
from packages.terminal.terminal import Terminal as _Terminal

terminal = _Terminal(_SubProcess())

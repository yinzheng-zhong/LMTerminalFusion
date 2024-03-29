from services.terminal.sub_process import SubProcess as _SubProcess
from services.terminal.terminal import Terminal as _Terminal

terminal = _Terminal(_SubProcess())

from packages.lm.api import API as _API
from packages.Env import env
from packages.lm.lm import LM as _LM

lm = _LM(
    _API(env=env)
)

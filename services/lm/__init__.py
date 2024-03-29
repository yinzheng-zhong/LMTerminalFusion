from services.lm.api import API as _API
from services.Env import env
from services.lm.lm import LM as _LM

lm = _LM(
    _API(env=env)
)

from switch_case import *
from operator import eq  # Sugar synthax
reason = (
    switch
    | case(_ == 'hambre') >> 'come'
    | case(_ == 'sed') >> 'bebe'
    | case(_ == 'vegiga llena') >> 'mea'
    | case(_ == 'apretón') >> 'caga'
    | case(_ == 'sueño') >> 'duerme'
    | case(_ == 200) >> 'OK'
    | case(_ == 500) >> 'ERROR'
    | case(_ /eq/ 200) >> 'OK'
    | case(_ /eq/ 500) >> 'ERROR'
    | case(_ /isinstance/ str)   >> "string"
    | case(_ /isinstance/ int)   >> "integer"
    | case(_ /isinstance/ float) >> "float"
    | case(_ /isinstance/ bool)  >> "bool"
    | default                    >> 'UNKNOWN')

assert reason('hambre') == 'come'
assert reason('sed') == 'bebe'
assert reason(200) == 'OK'
assert reason(500) == 'ERROR'
assert reason(42) == "integer"
assert reason("42") == "string"
assert reason(3.14) == "float"
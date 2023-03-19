import os

from pre_commit_example import random_function


def function(
    arg1: str,
    arg2: str,
    arg3: int,
    arg4: int,
    arg5: float,
    arg6: float,
    arg7: bool,
    arg8: bool,
) -> str:
    path = os.path.join(arg1, arg2, "abc", "efg", "hij")
    random_function(path)

    return "Function was called."

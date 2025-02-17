a: int = 1
b: float = 1.0
c: str = '1.0'
d: bool = 1

e: list[int] = [1, 2]
f: dict[str, bool] = {'Flag': True}

from typing import Literal
g: Literal["OK", "NG"] = "NG"

def sample(x: str) -> bool:
    return True


from typing import Dict

flag : bool = True

def greet(name: str) -> None:
    """Say hello to everyone"""
    print("Hi " + name)

greet('Manchester')
greet('Saddleworth')

x : Dict[str, float] = {"field1" : 2.0, "field2" : 3.0}
print(x)

from typing import Any, TypeVar

def first(xs : list[str]) -> str:
		return xs[0]

def first_int(xs : list[int]) -> int:
        return xs[0]

def first_any(xs : list[Any]) -> Any:
        return Any[0]

T = TypeVar('T')

def first_(xs : list[type(T)]) -> type(T)
    return xs[0]

y : Dict[str, float] = {"field1" : 2.0, "field2" : 3.0}
first(y)

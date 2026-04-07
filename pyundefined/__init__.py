from typing import TypeVar, Generic, Union

__version__ = "1.1.0"


class UndefinedType(object):
    """A type for representing the undefined value"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UndefinedType, cls).__new__(cls)
        return cls._instance

    def __repr__(self):
        return "undefined"

    # Python 2/3 Compatibility for Boolean Conversions
    def __nonzero__(self):
        return False

    def __bool__(self):
        return False

    def __eq__(self, other):
        return isinstance(other, UndefinedType)


undefined = UndefinedType()

T = TypeVar("T")

class MaybeUndefined(Generic[T]):
    def __init__(self, content):
        # type: (Union[T, UndefinedType]) -> None
        self.content = content

    def get(self):
        # type: () -> Union[T, UndefinedType]
        return self.content

    def set(self, value):
        # type: (Union[T, UndefinedType]) -> None
        self.content = value


class Nullable(Generic[T]):
    def __init__(self, content):
        # type: (Union[T, UndefinedType, None]) -> None
        self.content = content

    def get(self):
        # type: () -> Union[T, UndefinedType, None]
        return self.content

    def set(self, value):
        # type: (Union[T, UndefinedType, None]) -> None
        self.content = value

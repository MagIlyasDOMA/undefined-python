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

    def __hash__(self):
        return hash("undefined")


undefined = UndefinedType()
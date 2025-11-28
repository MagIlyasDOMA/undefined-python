class UndefinedType(object):
    """Тип для представления undefined значения"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UndefinedType, cls).__new__(cls)
        return cls._instance

    def __repr__(self):
        return "undefined"

    # Совместимость Python 2/3 для булевых преобразований
    def __nonzero__(self):
        return False

    def __bool__(self):
        return False

    def __eq__(self, other):
        return isinstance(other, UndefinedType)

    def __hash__(self):
        return hash("undefined")


undefined = UndefinedType()

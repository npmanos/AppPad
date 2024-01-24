from typing import Any


class singleton(type):
    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        else:
            instance = cls._instances[cls]
            if hasattr(cls, '__allow_reinit') and cls.__allow_reinit: #type: ignore
                instance.__init__(*args, **kwds)
        
        return instance


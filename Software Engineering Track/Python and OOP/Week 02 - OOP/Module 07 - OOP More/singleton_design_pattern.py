# Singleton -> one single instance respect to a class
# if you want a new instance, you will get the old one (already created) instance

class Singleton:
    _instance = None
    def __init__(self) -> None:
        if Singleton._instance is None:
            
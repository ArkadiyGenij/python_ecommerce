class ObjectCreationMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект класса {self.__class__.__name__}\n{repr(self)}")

    def __repr__(self):
        attrs = ', '.join([f"{value!r}" for value in self.__dict__.values()])
        return f"{self.__class__.__name__}({attrs})"

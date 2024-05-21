from src.modules.field import Field

class Main(Field):
    def __init__(self, main):
        super().__init__(main)
        self.main = Field(main)

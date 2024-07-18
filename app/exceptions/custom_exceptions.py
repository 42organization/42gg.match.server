class CustomException(Exception):
    def __init__(self, name: str, detail: str):
        self.name = name
        self.detail = detail
        super().__init__(self.detail)

    def __str__(self):
        return f'{self.name}: {self.detail}'
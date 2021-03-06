from typing import Literal

class Lambda:
    def invoke(self, *, FunctionName: str, Payload: str) -> object: ...

def client(name: Literal["lambda"], *, region_name: str) -> Lambda: ...

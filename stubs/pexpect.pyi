class Spawn:
    def expect(self, expected: str) -> int: ...
    def sendline(self, line: str) -> int: ...

def spawn(cmd: str) -> Spawn: ...
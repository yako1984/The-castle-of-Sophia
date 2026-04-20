# Mock de colorama para que el juego funcione sin la librería instalada
class MockColor:
    def __getattr__(self, name):
        return ""

Fore = MockColor()
Back = MockColor()
Style = MockColor()

def init(*args, **kwargs):
    pass

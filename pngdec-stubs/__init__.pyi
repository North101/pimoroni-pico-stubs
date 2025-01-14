from typing import Literal
from picographics import PicoGraphics


PNG_NORMAL = 0
PNG_POSTERISE = 0
PNG_DITHER = 1
PNG_COPY = 2

class PNG:
    def __init__(self, picographics: PicoGraphics):
        pass

    def __del__(self):
        pass

    def open_RAM(self, buffer: bytearray) -> bool:
        pass

    def open_file(self, filename: str) -> bool:
        pass

    def decode(self, x: int, y: int, scale: int|tuple[int, int], mode=PNG_NORMAL, source: tuple[int, int, int, int]|None=None, rotate: Literal[0]|Literal[90]|Literal[180]|Literal[270]=0):
        pass

    def get_width(self) -> int:
        pass

    def get_height(self) -> int:
        pass

    def get_palette(self) -> list[tuple[int, int, int]]:
        pass

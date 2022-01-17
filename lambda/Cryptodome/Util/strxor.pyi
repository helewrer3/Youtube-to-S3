from typing import Union, Optional

Buffer = Union[bytes, bytearray, memoryview]

def strxor(term1: bytes, term2: bytes, output: Optional[Buffer]=...) -> bytes: ...
def strxor_c(term: bytes, c: int, output: Optional[Buffer]=...) -> bytes: ...

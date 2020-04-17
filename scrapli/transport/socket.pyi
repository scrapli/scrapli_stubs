from scrapli.exceptions import ScrapliTimeout as ScrapliTimeout
from typing import Any

LOG: Any

class Socket:
    host: Any = ...
    port: Any = ...
    timeout: Any = ...
    sock: Any = ...
    def __init__(self, host: str, port: int, timeout: int) -> None: ...
    def __bool__(self) -> bool: ...
    def socket_open(self) -> None: ...
    def socket_close(self) -> None: ...
    def socket_isalive(self) -> bool: ...

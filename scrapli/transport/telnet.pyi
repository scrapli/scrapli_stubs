from scrapli.decorators import operation_timeout as operation_timeout
from scrapli.exceptions import ScrapliAuthenticationFailed as ScrapliAuthenticationFailed
from scrapli.helper import get_prompt_pattern as get_prompt_pattern, strip_ansi as strip_ansi
from scrapli.transport.transport import Transport as Transport
from telnetlib import Telnet
from typing import Any, Optional

LOG: Any
TELNET_TRANSPORT_ARGS: Any

class ScrapliTelnet(Telnet):
    eof: Any
    timeout: Any
    def __init__(self, host: str, port: int, timeout: int) -> None: ...

class TelnetTransport(Transport):
    auth_username: Any = ...
    auth_password: Any = ...
    username_prompt: str = ...
    password_prompt: str = ...
    session: Any
    lib_auth_exception: Any = ...
    def __init__(self, host: str, port: int=..., auth_username: str=..., auth_password: str=..., timeout_socket: int=..., timeout_transport: int=..., timeout_ops: int=..., timeout_exit: bool=..., keepalive: bool=..., keepalive_interval: int=..., keepalive_type: str=..., keepalive_pattern: str=..., comms_prompt_pattern: str=..., comms_return_char: str=..., comms_ansi: bool=...) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def isalive(self) -> bool: ...
    def read(self) -> bytes: ...
    def write(self, channel_input: str) -> None: ...
    def set_timeout(self, timeout: Optional[int]=...) -> None: ...
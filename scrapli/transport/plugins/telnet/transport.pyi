from scrapli.decorators import TransportTimeout as TransportTimeout
from scrapli.exceptions import ScrapliConnectionError as ScrapliConnectionError, ScrapliConnectionNotOpened as ScrapliConnectionNotOpened
from scrapli.transport.base import BasePluginTransportArgs as BasePluginTransportArgs, BaseTransportArgs as BaseTransportArgs, Transport as Transport
from telnetlib import Telnet
from typing import Any

class PluginTransportArgs(BasePluginTransportArgs): ...

class ScrapliTelnet(Telnet):
    eof: Any
    timeout: Any
    def __init__(self, host: str, port: int, timeout: float) -> None: ...

class TelnetTransport(Transport):
    plugin_transport_args: Any = ...
    username_prompt: str = ...
    password_prompt: str = ...
    session: Any = ...
    def __init__(self, base_transport_args: BaseTransportArgs, plugin_transport_args: PluginTransportArgs) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def isalive(self) -> bool: ...
    def read(self) -> bytes: ...
    def write(self, channel_input: bytes) -> None: ...

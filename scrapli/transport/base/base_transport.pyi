import abc
from abc import ABC, abstractmethod
from scrapli.logging import get_instance_logger as get_instance_logger
from typing import Any, Dict

class BaseTransportArgs:
    transport_options: Dict[str, Any]
    host: str
    port: int = ...
    timeout_socket: float = ...
    timeout_transport: float = ...
    logging_uid: str = ...
    def __init__(self, transport_options: Any, host: Any, port: Any, timeout_socket: Any, timeout_transport: Any, logging_uid: Any) -> None: ...

class BasePluginTransportArgs: ...

class BaseTransport(ABC, metaclass=abc.ABCMeta):
    _base_transport_args: Any = ...
    logger: Any = ...
    def __init__(self, base_transport_args: BaseTransportArgs) -> None: ...
    @abstractmethod
    def close(self) -> None: ...
    @abstractmethod
    def write(self, channel_input: bytes) -> None: ...
    @abstractmethod
    def isalive(self) -> bool: ...
    def _pre_open_closing_log(self, closing: bool=...) -> None: ...
    def _post_open_closing_log(self, closing: bool=...) -> None: ...

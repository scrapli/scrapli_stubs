import abc
from abc import ABC, abstractmethod
from scrapli.helper import attach_duplicate_log_filter as attach_duplicate_log_filter
from typing import Any

class TransportBase(ABC, metaclass=abc.ABCMeta):
    logger: Any = ...
    host: Any = ...
    port: Any = ...
    timeout_socket: Any = ...
    timeout_transport: Any = ...
    timeout_exit: Any = ...
    def __init__(self, host: str=..., port: int=..., timeout_socket: int=..., timeout_transport: int=..., timeout_exit: bool=...) -> None: ...
    def __bool__(self) -> bool: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    @abstractmethod
    def close(self) -> None: ...
    @abstractmethod
    def isalive(self) -> bool: ...
    @abstractmethod
    def set_timeout(self, timeout: int) -> None: ...

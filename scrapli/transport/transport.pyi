import abc
from abc import ABC, abstractmethod
from scrapli.transport.base_transport import TransportBase as TransportBase

class Transport(TransportBase, ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def open(self) -> None: ...
    @abstractmethod
    def read(self) -> bytes: ...
    @abstractmethod
    def write(self, channel_input: str) -> None: ...
    def _wait_for_session_fd_ready(self, fd: int) -> None: ...

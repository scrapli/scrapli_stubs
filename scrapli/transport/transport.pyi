import abc
from abc import ABC, abstractmethod
from scrapli.exceptions import ScrapliKeepaliveFailure as ScrapliKeepaliveFailure
from scrapli.transport.base_transport import TransportBase as TransportBase

class Transport(TransportBase, ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def open(self) -> None: ...
    @abstractmethod
    def read(self) -> bytes: ...
    @abstractmethod
    def write(self, channel_input: str) -> None: ...
    def _session_keepalive(self) -> None: ...
    def _keepalive_network(self) -> None: ...
    @abstractmethod
    def _keepalive_standard(self) -> None: ...

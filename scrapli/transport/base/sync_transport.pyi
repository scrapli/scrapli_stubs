import abc
from abc import ABC, abstractmethod
from scrapli.transport.base.base_transport import BaseTransport as BaseTransport

class Transport(BaseTransport, ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def open(self) -> None: ...
    @abstractmethod
    def read(self) -> bytes: ...

import abc
from abc import ABC, abstractmethod
from scrapli.transport.base_transport import TransportBase as TransportBase

class AsyncTransport(TransportBase, ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    async def open(self) -> None: ...
    @abstractmethod
    async def read(self) -> bytes: ...
    @abstractmethod
    def write(self, channel_input: str) -> None: ...

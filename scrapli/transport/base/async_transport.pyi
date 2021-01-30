import abc
from abc import ABC, abstractmethod
from scrapli.transport.base.base_transport import BaseTransport as BaseTransport

class AsyncTransport(BaseTransport, ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    async def open(self) -> None: ...
    @abstractmethod
    async def read(self) -> bytes: ...

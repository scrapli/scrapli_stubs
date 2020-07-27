from scrapli.channel import AsyncChannel as AsyncChannel
from scrapli.driver.base_driver import ASYNCIO_TRANSPORTS as ASYNCIO_TRANSPORTS, ScrapeBase as ScrapeBase
from scrapli.exceptions import TransportPluginError as TransportPluginError
from types import TracebackType
from typing import Any, Optional, Type

class AsyncScrape(ScrapeBase):
    channel: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    async def __aenter__(self) -> AsyncScrape: ...
    async def __aexit__(self, exception_type: Optional[Type[BaseException]], exception_value: Optional[BaseException], traceback: Optional[TracebackType]) -> None: ...
    async def open(self) -> None: ...
    async def close(self) -> None: ...

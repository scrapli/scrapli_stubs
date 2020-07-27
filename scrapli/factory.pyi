from scrapli.driver import AsyncGenericDriver as AsyncGenericDriver, AsyncNetworkDriver as AsyncNetworkDriver, GenericDriver as GenericDriver, NetworkDriver as NetworkDriver
from scrapli.driver.base_driver import ASYNCIO_TRANSPORTS as ASYNCIO_TRANSPORTS
from scrapli.driver.core import AsyncEOSDriver as AsyncEOSDriver, AsyncIOSXEDriver as AsyncIOSXEDriver, AsyncIOSXRDriver as AsyncIOSXRDriver, AsyncJunosDriver as AsyncJunosDriver, AsyncNXOSDriver as AsyncNXOSDriver, EOSDriver as EOSDriver, IOSXEDriver as IOSXEDriver, IOSXRDriver as IOSXRDriver, JunosDriver as JunosDriver, NXOSDriver as NXOSDriver
from scrapli.exceptions import ScrapliException as ScrapliException
from typing import Any, Dict, Optional, Tuple, Type, Union

LOG: Any
ASYNC_CORE_PLATFORM_MAP: Any
SYNC_CORE_PLATFORM_MAP: Any
ASYNC_DRIVER_MAP: Any
SYNC_DRIVER_MAP: Any

def _get_community_platform_details(community_platform_name: str) -> Dict[str, Any]: ...
def _get_community_driver(community_platform_name: str, variant: Optional[str], _async: bool=...) -> Tuple[Union[Type[AsyncNetworkDriver], Type[AsyncGenericDriver], Type[NetworkDriver], Type[GenericDriver]], Dict[str, Any]]: ...
def _get_driver(platform: str, variant: Optional[str], _async: bool=...) -> Tuple[Union[Type[NetworkDriver], Type[GenericDriver]], Dict[str, Any]]: ...

class Scrapli(NetworkDriver):
    def __new__(cls: Any, platform: str, variant: Optional[str]=..., **kwargs: Dict[Any, Any]) -> Scrapli: ...

class AsyncScrapli(AsyncNetworkDriver):
    def __new__(cls: Any, platform: str, variant: Optional[str]=..., **kwargs: Dict[Any, Any]) -> AsyncScrapli: ...

from scrapli.driver import AsyncNetworkDriver as AsyncNetworkDriver
from scrapli.driver.base_network_driver import PrivilegeLevel as PrivilegeLevel
from scrapli.driver.core.cisco_iosxe.base_driver import PRIVS as PRIVS
from typing import Any, Callable, Dict, List, Optional

async def iosxe_on_open(conn: AsyncNetworkDriver) -> None: ...
async def iosxe_on_close(conn: AsyncNetworkDriver) -> None: ...

class AsyncIOSXEDriver(AsyncNetworkDriver):
    def __init__(self, privilege_levels: Optional[Dict[str, PrivilegeLevel]]=..., default_desired_privilege_level: str=..., auth_secondary: str=..., on_open: Optional[Callable[..., Any]]=..., on_close: Optional[Callable[..., Any]]=..., textfsm_platform: str=..., genie_platform: str=..., failed_when_contains: Optional[List[str]]=..., **kwargs: Dict[str, Any]) -> None: ...

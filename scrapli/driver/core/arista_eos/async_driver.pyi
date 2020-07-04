from scrapli.driver import AsyncNetworkDriver as AsyncNetworkDriver
from scrapli.driver.base_network_driver import PrivilegeLevel as PrivilegeLevel
from scrapli.driver.core.arista_eos.base_driver import EOSDriverBase as EOSDriverBase, PRIVS as PRIVS
from typing import Any, Callable, Dict, List, Optional

async def eos_on_open(conn: AsyncNetworkDriver) -> None: ...
async def eos_on_close(conn: AsyncNetworkDriver) -> None: ...

class AsyncEOSDriver(AsyncNetworkDriver, EOSDriverBase):
    def __init__(self, privilege_levels: Optional[Dict[str, PrivilegeLevel]]=..., default_desired_privilege_level: str=..., auth_secondary: str=..., on_open: Optional[Callable[..., Any]]=..., on_close: Optional[Callable[..., Any]]=..., textfsm_platform: str=..., genie_platform: str=..., failed_when_contains: Optional[List[str]]=..., **kwargs: Dict[str, Any]) -> None: ...
    _current_priv_level: Any = ...
    async def _abort_config(self) -> None: ...
    def register_configuration_session(self, session_name: str) -> None: ...
from scrapli.driver import NetworkDriver as NetworkDriver
from scrapli.driver.base_network_driver import PrivilegeLevel as PrivilegeLevel
from scrapli.driver.core.cisco_iosxe.base_driver import PRIVS as PRIVS
from typing import Any, Callable, Dict, List, Optional

def iosxe_on_open(conn: NetworkDriver) -> None: ...
def iosxe_on_close(conn: NetworkDriver) -> None: ...

class IOSXEDriver(NetworkDriver):
    def __init__(self, privilege_levels: Optional[Dict[str, PrivilegeLevel]]=..., default_desired_privilege_level: str=..., auth_secondary: str=..., on_open: Optional[Callable[..., Any]]=..., on_close: Optional[Callable[..., Any]]=..., textfsm_platform: str=..., genie_platform: str=..., failed_when_contains: Optional[List[str]]=..., **kwargs: Dict[str, Any]) -> None: ...

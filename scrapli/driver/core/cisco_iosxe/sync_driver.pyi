from io import BytesIO
from scrapli.driver import NetworkDriver as NetworkDriver
from scrapli.driver.core.cisco_iosxe.base_driver import PRIVS as PRIVS
from scrapli.driver.network.base_driver import PrivilegeLevel as PrivilegeLevel
from typing import Any, Callable, Dict, List, Optional, Union

def iosxe_on_open(conn: NetworkDriver) -> None: ...
def iosxe_on_close(conn: NetworkDriver) -> None: ...

class IOSXEDriver(NetworkDriver):
    def __init__(self, host: str, privilege_levels: Optional[Dict[str, PrivilegeLevel]]=..., default_desired_privilege_level: str=..., port: int=..., auth_username: str=..., auth_password: str=..., auth_private_key: str=..., auth_private_key_passphrase: str=..., auth_strict_key: bool=..., auth_bypass: bool=..., timeout_socket: float=..., timeout_transport: float=..., timeout_ops: float=..., comms_return_char: str=..., comms_ansi: bool=..., ssh_config_file: Union[str, bool]=..., ssh_known_hosts_file: Union[str, bool]=..., on_init: Optional[Callable[..., Any]]=..., on_open: Optional[Callable[..., Any]]=..., on_close: Optional[Callable[..., Any]]=..., transport: str=..., transport_options: Optional[Dict[str, Any]]=..., channel_log: Union[str, bool, BytesIO]=..., channel_lock: bool=..., logging_uid: str=..., auth_secondary: str=..., failed_when_contains: Optional[List[str]]=..., textfsm_platform: str=..., genie_platform: str=...) -> None: ...

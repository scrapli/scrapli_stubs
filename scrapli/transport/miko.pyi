from scrapli.exceptions import KeyVerificationFailed as KeyVerificationFailed, MissingDependencies as MissingDependencies, ScrapliAuthenticationFailed as ScrapliAuthenticationFailed
from scrapli.ssh_config import SSHConfig as SSHConfig, SSHKnownHosts as SSHKnownHosts
from scrapli.transport.socket import Socket as Socket
from scrapli.transport.transport import Transport as Transport
from typing import Any, Optional

LOG: Any
MIKO_TRANSPORT_ARGS: Any

class MikoTransport(Transport):
    auth_username: Any = ...
    auth_private_key: Any = ...
    auth_password: Any = ...
    auth_strict_key: Any = ...
    ssh_known_hosts_file: Any = ...
    session_lock: Any = ...
    lib_session: Any = ...
    session: Any = ...
    channel: Any = ...
    lib_auth_exception: Any = ...
    socket: Any = ...
    def __init__(self, host: str, port: int=..., auth_username: str=..., auth_private_key: str=..., auth_password: str=..., auth_strict_key: bool=..., timeout_socket: int=..., timeout_transport: int=..., timeout_exit: bool=..., keepalive: bool=..., keepalive_interval: int=..., keepalive_type: str=..., keepalive_pattern: str=..., ssh_config_file: str=..., ssh_known_hosts_file: str=...) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def isalive(self) -> bool: ...
    def read(self) -> bytes: ...
    def write(self, channel_input: str) -> None: ...
    def set_timeout(self, timeout: Optional[int]=...) -> None: ...

from scrapli.exceptions import ScrapliAuthenticationFailed as ScrapliAuthenticationFailed, ScrapliConnectionError as ScrapliConnectionError, ScrapliConnectionNotOpened as ScrapliConnectionNotOpened
from scrapli.ssh_config import SSHKnownHosts as SSHKnownHosts
from scrapli.transport.base import BasePluginTransportArgs as BasePluginTransportArgs, BaseTransportArgs as BaseTransportArgs, Transport as Transport
from scrapli.transport.base.base_socket import Socket as Socket
from ssh2.channel import Channel as Channel
from typing import Any

class PluginTransportArgs(BasePluginTransportArgs):
    auth_username: str
    auth_password: str = ...
    auth_private_key: str = ...
    auth_strict_key: bool = ...
    ssh_config_file: str = ...
    ssh_known_hosts_file: str = ...
    def __init__(self, auth_username: Any, auth_password: Any, auth_private_key: Any, auth_strict_key: Any, ssh_config_file: Any, ssh_known_hosts_file: Any) -> None: ...

class Ssh2Transport(Transport):
    plugin_transport_args: Any = ...
    socket: Any = ...
    session: Any = ...
    session_channel: Any = ...
    def __init__(self, base_transport_args: BaseTransportArgs, plugin_transport_args: PluginTransportArgs) -> None: ...
    def open(self) -> None: ...
    def _verify_key(self) -> None: ...
    def _authenticate(self) -> None: ...
    def _authenticate_public_key(self) -> None: ...
    def _authenticate_password(self) -> None: ...
    def _open_channel(self) -> None: ...
    def close(self) -> None: ...
    def isalive(self) -> bool: ...
    def read(self) -> bytes: ...
    def write(self, channel_input: bytes) -> None: ...
    def _set_timeout(self, value: float) -> None: ...
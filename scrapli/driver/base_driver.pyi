from scrapli.channel import CHANNEL_ARGS as CHANNEL_ARGS
from scrapli.exceptions import UnsupportedPlatform as UnsupportedPlatform
from scrapli.helper import _find_transport_plugin as _find_transport_plugin, resolve_ssh_config as resolve_ssh_config, resolve_ssh_known_hosts as resolve_ssh_known_hosts
from scrapli.transport import SYSTEM_SSH_TRANSPORT_ARGS as SYSTEM_SSH_TRANSPORT_ARGS, SystemSSHTransport as SystemSSHTransport, TELNET_TRANSPORT_ARGS as TELNET_TRANSPORT_ARGS, TelnetTransport as TelnetTransport, Transport as Transport
from typing import Any, Callable, Dict, Optional, Tuple, Union

TRANSPORT_CLASS: Dict[str, Callable[..., Transport]]
TRANSPORT_ARGS: Dict[str, Tuple[str, ...]]
TRANSPORT_BASE_ARGS: Any

class ScrapeBase:
    _initialization_args: Any = ...
    logger: Any = ...
    _transport: Any = ...
    transport: Any = ...
    channel_args: Any = ...
    def __init__(self, host: str=..., port: int=..., auth_username: str=..., auth_password: str=..., auth_private_key: str=..., auth_private_key_passphrase: str=..., auth_strict_key: bool=..., auth_bypass: bool=..., timeout_socket: int=..., timeout_transport: int=..., timeout_ops: int=..., timeout_exit: bool=..., keepalive: bool=..., keepalive_interval: int=..., keepalive_type: str=..., keepalive_pattern: str=..., comms_prompt_pattern: str=..., comms_return_char: str=..., comms_ansi: bool=..., ssh_config_file: Union[str, bool]=..., ssh_known_hosts_file: Union[str, bool]=..., on_open: Optional[Callable[..., Any]]=..., on_close: Optional[Callable[..., Any]]=..., transport: str=..., transport_options: Optional[Dict[str, Any]]=...) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    _host: Any = ...
    def _setup_host(self, host: str, port: int) -> None: ...
    def _setup_auth(self, auth_username: str, auth_password: str, auth_private_key: str, auth_private_key_passphrase: str, auth_strict_key: bool, auth_bypass: bool) -> None: ...
    def _setup_timeouts(self, timeout_socket: int, timeout_transport: int, timeout_ops: int, timeout_exit: bool) -> None: ...
    def _setup_keepalive(self, keepalive: bool, keepalive_type: str, keepalive_interval: int, keepalive_pattern: str) -> None: ...
    def _setup_comms(self, comms_prompt_pattern: str, comms_return_char: str, comms_ansi: bool) -> None: ...
    on_open: Any = ...
    on_close: Any = ...
    def _setup_callables(self, on_open: Optional[Callable[..., Any]], on_close: Optional[Callable[..., Any]]) -> None: ...
    def _setup_ssh_args(self, ssh_config_file: Union[str, bool], ssh_known_hosts_file: Union[str, bool]) -> None: ...
    def _transport_factory(self, transport: str) -> Tuple[Callable[..., Any], Dict[str, Any]]: ...
    def isalive(self) -> bool: ...

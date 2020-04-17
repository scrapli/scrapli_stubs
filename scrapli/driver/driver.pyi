from scrapli.channel import CHANNEL_ARGS as CHANNEL_ARGS, Channel as Channel
from scrapli.helper import resolve_ssh_config as resolve_ssh_config, resolve_ssh_known_hosts as resolve_ssh_known_hosts
from scrapli.transport import MIKO_TRANSPORT_ARGS as MIKO_TRANSPORT_ARGS, MikoTransport as MikoTransport, SSH2Transport as SSH2Transport, SSH2_TRANSPORT_ARGS as SSH2_TRANSPORT_ARGS, SYSTEM_SSH_TRANSPORT_ARGS as SYSTEM_SSH_TRANSPORT_ARGS, SystemSSHTransport as SystemSSHTransport, TELNET_TRANSPORT_ARGS as TELNET_TRANSPORT_ARGS, TelnetTransport as TelnetTransport, Transport as Transport
from types import TracebackType
from typing import Any, Callable, Dict, Optional, Tuple, Type, Union

TRANSPORT_CLASS: Dict[str, Callable[..., Transport]]
TRANSPORT_ARGS: Dict[str, Tuple[str, ...]]
TRANSPORT_BASE_ARGS: Any
LOG: Any

class Scrape:
    transport: Any = ...
    channel_args: Any = ...
    channel: Any = ...
    def __init__(self, host: str=..., port: int=..., auth_username: str=..., auth_password: str=..., auth_private_key: str=..., auth_strict_key: bool=..., auth_bypass: bool=..., timeout_socket: int=..., timeout_transport: int=..., timeout_ops: int=..., timeout_exit: bool=..., keepalive: bool=..., keepalive_interval: int=..., keepalive_type: str=..., keepalive_pattern: str=..., comms_prompt_pattern: str=..., comms_return_char: str=..., comms_ansi: bool=..., ssh_config_file: Union[str, bool]=..., ssh_known_hosts_file: Union[str, bool]=..., on_open: Optional[Callable[..., Any]]=..., on_close: Optional[Callable[..., Any]]=..., transport: str=...) -> None: ...
    def __enter__(self) -> Scrape: ...
    def __exit__(self, exception_type: Optional[Type[BaseException]], exception_value: Optional[BaseException], traceback: Optional[TracebackType]) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def isalive(self) -> bool: ...

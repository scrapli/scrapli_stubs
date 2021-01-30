from io import BytesIO
from scrapli.driver.generic import GenericDriver as GenericDriver
from scrapli.driver.network.base_driver import BaseNetworkDriver as BaseNetworkDriver, PrivilegeAction as PrivilegeAction, PrivilegeLevel as PrivilegeLevel
from scrapli.exceptions import ScrapliPrivilegeError as ScrapliPrivilegeError
from scrapli.response import MultiResponse as MultiResponse, Response as Response
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

class NetworkDriver(GenericDriver, BaseNetworkDriver):
    comms_prompt_pattern: Any
    auth_secondary: Any = ...
    failed_when_contains: Any = ...
    textfsm_platform: Any = ...
    genie_platform: Any = ...
    privilege_levels: Any = ...
    default_desired_privilege_level: Any = ...
    _priv_graph: Any = ...
    def __init__(self, host: str, privilege_levels: Dict[str, PrivilegeLevel], default_desired_privilege_level: str, port: int=..., auth_username: str=..., auth_password: str=..., auth_private_key: str=..., auth_private_key_passphrase: str=..., auth_strict_key: bool=..., auth_bypass: bool=..., timeout_socket: float=..., timeout_transport: float=..., timeout_ops: float=..., comms_return_char: str=..., comms_ansi: bool=..., ssh_config_file: Union[str, bool]=..., ssh_known_hosts_file: Union[str, bool]=..., on_init: Optional[Callable[..., Any]]=..., on_open: Optional[Callable[..., Any]]=..., on_close: Optional[Callable[..., Any]]=..., transport: str=..., transport_options: Optional[Dict[str, Any]]=..., channel_log: Union[str, bool, BytesIO]=..., channel_lock: bool=..., logging_uid: str=..., auth_secondary: str=..., failed_when_contains: Optional[List[str]]=..., textfsm_platform: str=..., genie_platform: str=...) -> None: ...
    def _escalate(self, escalate_priv: PrivilegeLevel) -> None: ...
    def _deescalate(self, current_priv: PrivilegeLevel) -> None: ...
    _current_priv_level: Any = ...
    def acquire_priv(self, desired_priv: str) -> None: ...
    def send_command(self, command: str, *, strip_prompt: bool=..., failed_when_contains: Optional[Union[str, List[str]]]=..., timeout_ops: Optional[float]=...) -> Response: ...
    def send_commands(self, commands: List[str], *, strip_prompt: bool=..., failed_when_contains: Optional[Union[str, List[str]]]=..., stop_on_failed: bool=..., eager: bool=..., timeout_ops: Optional[float]=...) -> MultiResponse: ...
    def send_commands_from_file(self, file: str, *, strip_prompt: bool=..., failed_when_contains: Optional[Union[str, List[str]]]=..., stop_on_failed: bool=..., eager: bool=..., timeout_ops: Optional[float]=...) -> MultiResponse: ...
    def send_interactive(self, interact_events: List[Tuple[str, str, Optional[bool]]], *, failed_when_contains: Optional[Union[str, List[str]]]=..., privilege_level: str=..., timeout_ops: Optional[float]=...) -> Response: ...
    def _abort_config(self) -> None: ...
    def send_configs(self, configs: List[str], *, strip_prompt: bool=..., failed_when_contains: Optional[Union[str, List[str]]]=..., stop_on_failed: bool=..., privilege_level: str=..., eager: bool=..., timeout_ops: Optional[float]=...) -> MultiResponse: ...
    def send_config(self, config: str, *, strip_prompt: bool=..., failed_when_contains: Optional[Union[str, List[str]]]=..., stop_on_failed: bool=..., privilege_level: str=..., eager: bool=..., timeout_ops: Optional[float]=...) -> Response: ...
    def send_configs_from_file(self, file: str, *, strip_prompt: bool=..., failed_when_contains: Optional[Union[str, List[str]]]=..., stop_on_failed: bool=..., privilege_level: str=..., eager: bool=..., timeout_ops: Optional[float]=...) -> MultiResponse: ...

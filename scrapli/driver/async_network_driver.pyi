from collections import UserList
from scrapli.driver.async_generic_driver import AsyncGenericDriver as AsyncGenericDriver
from scrapli.driver.base_network_driver import NetworkDriverBase as NetworkDriverBase, PrivilegeAction as PrivilegeAction, PrivilegeLevel as PrivilegeLevel
from scrapli.exceptions import CouldNotAcquirePrivLevel as CouldNotAcquirePrivLevel
from scrapli.response import MultiResponse as MultiResponse, Response as Response
from typing import Any, Dict, List, Optional, Tuple, Union

ScrapliMultiResponse = UserList[Response]

class AsyncNetworkDriver(AsyncGenericDriver, NetworkDriverBase):
    auth_secondary: Any = ...
    privilege_levels: Any = ...
    _priv_map: Any = ...
    default_desired_privilege_level: Any = ...
    textfsm_platform: Any = ...
    genie_platform: Any = ...
    failed_when_contains: Any = ...
    def __init__(self, privilege_levels: Dict[str, PrivilegeLevel], default_desired_privilege_level: str, auth_secondary: str=..., failed_when_contains: Optional[List[str]]=..., textfsm_platform: str=..., genie_platform: str=..., **kwargs: Any) -> None: ...
    async def _escalate(self, escalate_priv: PrivilegeLevel) -> None: ...
    async def _deescalate(self, current_priv: PrivilegeLevel) -> None: ...
    _current_priv_level: Any = ...
    async def acquire_priv(self, desired_priv: str) -> None: ...
    async def send_command(self, command: str, strip_prompt: bool=..., failed_when_contains: Optional[Union[str, List[str]]]=...) -> Response: ...
    async def send_commands(self, commands: List[str], strip_prompt: bool=..., failed_when_contains: Optional[Union[str, List[str]]]=..., stop_on_failed: bool=...) -> ScrapliMultiResponse: ...
    async def send_commands_from_file(self, file: str, strip_prompt: bool=..., failed_when_contains: Optional[Union[str, List[str]]]=..., stop_on_failed: bool=...) -> ScrapliMultiResponse: ...
    async def send_interactive(self, interact_events: List[Tuple[str, str, Optional[bool]]], failed_when_contains: Optional[Union[str, List[str]]]=..., privilege_level: str=...) -> Response: ...
    async def _abort_config(self) -> None: ...
    async def send_config(self, config: str, strip_prompt: bool=..., failed_when_contains: Optional[Union[str, List[str]]]=..., stop_on_failed: bool=..., privilege_level: str=...) -> Response: ...
    async def send_configs(self, configs: List[str], strip_prompt: bool=..., failed_when_contains: Optional[Union[str, List[str]]]=..., stop_on_failed: bool=..., privilege_level: str=...) -> ScrapliMultiResponse: ...
    async def send_configs_from_file(self, file: str, strip_prompt: bool=..., failed_when_contains: Optional[Union[str, List[str]]]=..., stop_on_failed: bool=..., privilege_level: str=...) -> ScrapliMultiResponse: ...

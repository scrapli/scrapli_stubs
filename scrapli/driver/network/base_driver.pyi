from enum import Enum
from logging import LoggerAdapter
from scrapli.exceptions import ScrapliPrivilegeError as ScrapliPrivilegeError, ScrapliTypeError as ScrapliTypeError
from scrapli.helper import user_warning as user_warning
from scrapli.response import MultiResponse as MultiResponse, Response as Response
from typing import Any, DefaultDict, Dict, List, Optional, Set, Tuple, Union

class PrivilegeLevel:
    __slots__: Any = ...
    pattern: Any = ...
    name: Any = ...
    previous_priv: Any = ...
    deescalate: Any = ...
    escalate: Any = ...
    escalate_auth: Any = ...
    escalate_prompt: Any = ...
    def __init__(self, pattern: str, name: str, previous_priv: str, deescalate: str, escalate: str, escalate_auth: bool, escalate_prompt: str) -> None: ...

DUMMY_PRIV_LEVEL: Any
PRIVS: Dict[str, PrivilegeLevel]

class PrivilegeAction(Enum):
    NO_ACTION: str = ...
    ESCALATE: str = ...
    DEESCALATE: str = ...

class BaseNetworkDriver:
    logger: LoggerAdapter
    auth_secondary: str
    failed_when_contains: List[str]
    textfsm_platform: str
    genie_platform: str
    privilege_levels: Dict[str, PrivilegeLevel]
    comms_prompt_pattern: str
    _current_priv_level: Any = ...
    _priv_graph: DefaultDict[str, Set[str]]
    def _generate_comms_prompt_pattern(self) -> None: ...
    def _determine_current_priv(self, current_prompt: str) -> List[str]: ...
    def _build_priv_graph(self) -> None: ...
    def _build_priv_change_map(self, starting_priv_name: str, destination_priv_name: str, priv_change_map: Optional[List[str]]=...) -> List[str]: ...
    def update_privilege_levels(self) -> None: ...
    def _validate_privilege_level_name(self, privilege_level_name: str) -> None: ...
    def _pre_escalate(self, escalate_priv: PrivilegeLevel) -> None: ...
    def _process_acquire_priv(self, destination_priv: str, current_prompt: str) -> Tuple[PrivilegeAction, PrivilegeLevel]: ...
    def _update_response(self, response: Response) -> None: ...
    @staticmethod
    def _pre_send_config(config: str) -> List[str]: ...
    def _post_send_config(self, config: str, multi_response: MultiResponse) -> Response: ...
    def _pre_send_configs(self, configs: List[str], failed_when_contains: Optional[Union[str, List[str]]]=..., privilege_level: str=...) -> Tuple[str, Union[str, List[str]]]: ...
    def _post_send_configs(self, responses: MultiResponse) -> MultiResponse: ...

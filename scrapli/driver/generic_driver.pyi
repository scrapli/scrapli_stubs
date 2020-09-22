from collections import UserList
from scrapli.channel import Channel as Channel
from scrapli.decorators import TimeoutModifier as TimeoutModifier
from scrapli.driver.base_generic_driver import GenericDriverBase as GenericDriverBase
from scrapli.driver.driver import Scrape as Scrape
from scrapli.response import Response as Response
from typing import Any, List, Optional, Tuple, Union

ScrapliMultiResponse = UserList[Response]

class GenericDriver(Scrape, GenericDriverBase):
    channel: Any
    def __init__(self, comms_prompt_pattern: str=..., comms_ansi: bool=..., **kwargs: Any) -> None: ...
    def get_prompt(self) -> str: ...
    def _send_command_eager(self, command: str, strip_prompt: bool=..., failed_when_contains: Optional[Union[str, List[str]]]=..., *, timeout_ops: Optional[float]=...) -> Response: ...
    def send_command(self, command: str, strip_prompt: bool=..., failed_when_contains: Optional[Union[str, List[str]]]=..., *, timeout_ops: Optional[float]=...) -> Response: ...
    def send_commands(self, commands: List[str], strip_prompt: bool=..., failed_when_contains: Optional[Union[str, List[str]]]=..., stop_on_failed: bool=..., *, timeout_ops: Optional[float]=...) -> ScrapliMultiResponse: ...
    def send_commands_from_file(self, file: str, strip_prompt: bool=..., failed_when_contains: Optional[Union[str, List[str]]]=..., stop_on_failed: bool=..., *, timeout_ops: Optional[float]=...) -> ScrapliMultiResponse: ...
    def send_interactive(self, interact_events: List[Tuple[str, str, Optional[bool]]], failed_when_contains: Optional[Union[str, List[str]]]=..., privilege_level: str=...) -> Response: ...
    def send_and_read(self, channel_input: str, expected_outputs: Optional[List[str]]=..., strip_prompt: bool=..., failed_when_contains: Optional[Union[str, List[str]]]=..., *, timeout_ops: Optional[float]=..., read_duration: float=...) -> Response: ...

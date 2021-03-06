from collections import UserList
from io import TextIOWrapper
from scrapli.exceptions import ScrapliCommandFailure as ScrapliCommandFailure
from scrapli.helper import _textfsm_get_template as _textfsm_get_template, genie_parse as genie_parse, textfsm_parse as textfsm_parse, ttp_parse as ttp_parse
from typing import Any, Dict, List, Optional, Union

class Response:
    host: Any = ...
    start_time: Any = ...
    finish_time: Any = ...
    elapsed_time: Any = ...
    channel_input: Any = ...
    textfsm_platform: Any = ...
    genie_platform: Any = ...
    raw_result: bytes = ...
    result: str = ...
    failed_when_contains: Any = ...
    failed: bool = ...
    def __init__(self, host: str, channel_input: str, textfsm_platform: str=..., genie_platform: str=..., failed_when_contains: Optional[Union[str, List[str]]]=...) -> None: ...
    def __bool__(self) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def record_response(self, result: bytes) -> None: ...
    def textfsm_parse_output(self, to_dict: bool=...) -> Union[Dict[str, Any], List[Any]]: ...
    def genie_parse_output(self) -> Union[Dict[str, Any], List[Any]]: ...
    def ttp_parse_output(self, template: Union[str, TextIOWrapper]) -> Union[Dict[str, Any], List[Any]]: ...
    def raise_for_status(self) -> None: ...
ScrapliMultiResponse = UserList[Response]

class MultiResponse(ScrapliMultiResponse):
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    @property
    def failed(self) -> bool: ...
    @property
    def result(self) -> str: ...
    def raise_for_status(self) -> None: ...

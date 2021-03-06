from scrapli.exceptions import ScrapliTypeError as ScrapliTypeError
from scrapli.helper import resolve_file as resolve_file
from scrapli.response import MultiResponse as MultiResponse, Response as Response
from typing import Any, List, Optional, Tuple, Union

class BaseGenericDriver:
    @staticmethod
    def _pre_send_command(host: str, command: str, failed_when_contains: Optional[Union[str, List[str]]]=...) -> Response: ...
    @staticmethod
    def _post_send_command(raw_response: bytes, processed_response: bytes, response: Response) -> Response: ...
    @staticmethod
    def _pre_send_commands(commands: List[str]) -> MultiResponse: ...
    @staticmethod
    def _pre_send_from_file(file: str, caller: str) -> List[str]: ...
    @classmethod
    def _pre_send_interactive(cls: Any, host: str, interact_events: List[Tuple[str, str, Optional[bool]]], failed_when_contains: Optional[Union[str, List[str]]]=...) -> Response: ...

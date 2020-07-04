from abc import ABC
from scrapli.helper import get_prompt_pattern as get_prompt_pattern, normalize_lines as normalize_lines
from scrapli.transport.async_transport import AsyncTransport as AsyncTransport
from scrapli.transport.transport import Transport as Transport
from typing import Any, List, Optional, Tuple, Union

CHANNEL_ARGS: Any

class ChannelBase(ABC):
    logger: Any = ...
    transport: Any = ...
    comms_prompt_pattern: Any = ...
    comms_return_char: Any = ...
    comms_ansi: Any = ...
    comms_auto_expand: Any = ...
    timeout_ops: Any = ...
    def __init__(self, transport: Union[Transport, AsyncTransport], comms_prompt_pattern: str=..., comms_return_char: str=..., comms_ansi: bool=..., comms_auto_expand: bool=..., timeout_ops: int=...) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def _restructure_output(self, output: bytes, strip_prompt: bool=...) -> bytes: ...
    @staticmethod
    def _process_auto_expand(output: bytes, channel_input: bytes) -> bool: ...
    def _send_return(self) -> None: ...
    @staticmethod
    def _pre_send_input(channel_input: str) -> None: ...
    @staticmethod
    def _pre_send_inputs_interact(interact_events: List[Tuple[str, str, Optional[bool]]]) -> None: ...
    def _post_send_inputs_interact(self, output: bytes) -> Tuple[bytes, bytes]: ...

from scrapli.decorators import operation_timeout as operation_timeout
from scrapli.helper import get_prompt_pattern as get_prompt_pattern, normalize_lines as normalize_lines, strip_ansi as strip_ansi
from scrapli.transport.transport import Transport as Transport
from typing import Any, List, Optional, Tuple

LOG: Any
CHANNEL_ARGS: Any

class Channel:
    transport: Any = ...
    comms_prompt_pattern: Any = ...
    comms_return_char: Any = ...
    comms_ansi: Any = ...
    timeout_ops: Any = ...
    def __init__(self, transport: Transport, comms_prompt_pattern: str=..., comms_return_char: str=..., comms_ansi: bool=..., timeout_ops: int=...) -> None: ...
    def get_prompt(self) -> str: ...
    def send_input(self, channel_input: str, strip_prompt: bool=...) -> Tuple[str, str]: ...
    def send_inputs_interact(self, interact_events: List[Tuple[str, str, Optional[bool]]]) -> Tuple[str, str]: ...

from scrapli.channel.base_channel import ChannelBase as ChannelBase
from scrapli.decorators import OperationTimeout as OperationTimeout
from scrapli.helper import get_prompt_pattern as get_prompt_pattern, strip_ansi as strip_ansi
from scrapli.transport.async_transport import AsyncTransport as AsyncTransport
from typing import Any, List, Optional, Tuple

class AsyncChannel(ChannelBase):
    transport: Any
    def __init__(self, transport: AsyncTransport, **kwargs: Any) -> None: ...
    async def _read_chunk(self) -> bytes: ...
    async def _read_until_input(self, channel_input: bytes, auto_expand: Optional[bool]=...) -> bytes: ...
    async def _read_until_prompt(self, output: bytes=..., prompt: str=...) -> bytes: ...
    async def get_prompt(self) -> str: ...
    async def send_input(self, channel_input: str, strip_prompt: bool=...) -> Tuple[bytes, bytes]: ...
    async def _async_send_input(self, channel_input: str, strip_prompt: bool) -> Tuple[bytes, bytes]: ...
    async def send_inputs_interact(self, interact_events: List[Tuple[str, str, Optional[bool]]]) -> Tuple[bytes, bytes]: ...

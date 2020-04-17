from scrapli.channel import Channel as Channel
from scrapli.transport import Transport as Transport
from typing import Any, Callable

LOG: Any

def operation_timeout(attribute: str, message: str=...) -> Callable[..., Any]: ...

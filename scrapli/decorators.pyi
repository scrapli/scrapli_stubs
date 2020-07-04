from scrapli.channel import Channel as Channel
from scrapli.exceptions import ConnectionNotOpened as ConnectionNotOpened, ScrapliTimeout as ScrapliTimeout
from scrapli.transport import Transport as Transport
from typing import Any, Callable

def operation_timeout(attribute: str, message: str=...) -> Callable[..., Any]: ...
def requires_open_session() -> Callable[..., Any]: ...

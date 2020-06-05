import logging
from scrapli.driver import AsyncScrape as AsyncScrape, Scrape as Scrape
from typing import Any

__version__: str

class DuplicateFilter(logging.Filter):
    last_log: Any = ...
    def __init__(self) -> None: ...
    def filter(self, record: logging.LogRecord) -> bool: ...

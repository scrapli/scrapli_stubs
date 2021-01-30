from scrapli.driver.network.base_driver import PrivilegeLevel as PrivilegeLevel
from scrapli.exceptions import ScrapliValueError as ScrapliValueError
from typing import Any, Dict

PRIVS: Any

class EOSDriverBase:
    privilege_levels: Dict[str, PrivilegeLevel]
    def _create_configuration_session(self, session_name: str) -> None: ...

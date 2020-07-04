from typing import Any, Dict, Optional

HOST_ATTRS: Any

class SSHConfig:
    ssh_config_file: Any = ...
    ssh_config: Any = ...
    hosts: Any = ...
    def __init__(self, ssh_config_file: str) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bool__(self) -> bool: ...
    @staticmethod
    def _strip_comments(line: str) -> str: ...
    def _parse(self) -> Dict[str, Host]: ...
    def _merge_hosts(self) -> None: ...
    def _lookup_fuzzy_match(self, host: str, hosts: Optional[Dict[str, Host]]=...) -> str: ...
    def lookup(self, host: str) -> Host: ...

class Host:
    hosts: str = ...
    hostname: Any = ...
    port: Any = ...
    user: str = ...
    address_family: Any = ...
    bind_address: Any = ...
    connect_timeout: Any = ...
    identities_only: Any = ...
    identity_file: Any = ...
    keyboard_interactive: Any = ...
    password_authentication: Any = ...
    preferred_authentication: Any = ...
    def __init__(self) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class SSHKnownHosts:
    ssh_known_hosts_file: Any = ...
    ssh_known_hosts: Any = ...
    hosts: Any = ...
    def __init__(self, ssh_known_hosts_file: str) -> None: ...
    def _parse(self) -> Dict[str, Dict[str, str]]: ...

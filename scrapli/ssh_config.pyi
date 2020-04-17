from typing import Any

class SSHConfig:
    ssh_config_file: Any = ...
    ssh_config: Any = ...
    hosts: Any = ...
    def __init__(self, ssh_config_file: str) -> None: ...
    def __bool__(self) -> bool: ...
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

class SSHKnownHosts:
    ssh_known_hosts_file: Any = ...
    ssh_known_hosts: Any = ...
    hosts: Any = ...
    def __init__(self, ssh_known_hosts_file: str) -> None: ...
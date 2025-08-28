 
 import pytest
 from pydantic import ValidationError
 from wazuh.core.config.models.server import (
     DEFAULT_CTI_URL,
     CTIConfig,
     [
         (
             {
                'jwt': {'public_key': 'value', 'private_key': 'value'},
             },
             {
                 'update_check': False,
             },
         )
     ],
 def test_server_config_default_values(file_path_validation_mock, init_values, expected):
     """Check the correct initialization of the `ServerConfig` class."""
     config = ServerConfig(**init_values)
    assert config.jwt == expected['jwt']
     assert config.update_check == expected['update_check']
 
 
 def test_server_config_invalid_values():
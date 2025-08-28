 
 mock_config_data = {
     'server': {
        'port': 1516,
        'bind_addr': '0.0.0.0',
        'nodes': ['node1'],
        'node': {'name': 'example', 'type': 'master', 'ssl': {'key': 'value', 'cert': 'value', 'ca': 'value'}},
        'worker': {},
        'master': {},
        'communications': {},
         'logging': {'level': 'debug2'},
         'cti': {},
     },
 
 @pytest.fixture
 def patch_load():
    """Patch the load method in CentralizedConfig"""
     with patch.object(CentralizedConfig, 'load', return_value=None):
         with patch.object(ValidateFilePathMixin, '_validate_file_path', return_value=None):
             CentralizedConfig._config = Config(**mock_config_data)
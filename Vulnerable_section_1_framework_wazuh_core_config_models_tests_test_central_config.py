                     'username': 'user_example',
                     'password': 'password_example',
                 },
                'server': {
                    'nodes': ['master'],
                    'node': {
                        'name': 'example',
                        'type': 'master',
                        'ssl': {'key': 'value', 'cert': 'value', 'ca': 'value'},
                    },
                },
             },
             {
                'node': {'name': 'example', 'type': 'master', 'ssl': {'key': 'value', 'cert': 'value', 'ca': 'value'}},
                 'server': {
                    'nodes': ['master'],
                    'port': 1516,
                    'bind_addr': 'localhost',
                    'hidden': False,
                     'update_check': False,
                     'logging.level': 'info',
                 },
     with patch.object(ValidateFilePathMixin, '_validate_file_path', return_value=None):
         config = Config(**init_values)
 
        assert config.server.port == expected['server']['port']
        assert config.server.bind_addr == expected['server']['bind_addr']
        assert config.server.hidden == expected['server']['hidden']
         assert config.server.update_check == expected['server']['update_check']
         assert config.server.logging.level == expected['server']['logging.level']
 
 
 #originally, this was app = create_app('DelopmentConfig')
 #app = create_app('ProductionConfig')
 config_name = 'ProductionConfig'
 app = create_app(config_name)

 
 logging.basicConfig(level=logging.DEBUG)
 app.logger.info("Flask app initialized with Production configuration.")
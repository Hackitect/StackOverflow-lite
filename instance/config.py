'''
This files holds the configuration file our APP
will enable us to instanciate different instances of our app
e.g. we can either start the app in development mode, production or testing mode
'''

class Config():
    ''' default mode '''
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'dev'

class DevelopmentConfig():
    DEBUG = True

class ProductionConfig():
    DEBUG = False
    TESTING = False

class TestingConfig():
    DEBUG = True
    TESTING = True

app_config = dict(
    development = DevelopmentConfig,
    testing = TestingConfig,
    production = ProductionConfig
)
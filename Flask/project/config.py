# Configuraciones Globales
class Config:
    pass

# Configuraciones especificas
class DevelopmentConfig(Config):
    DEBUG = True

config = {

    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')

    @staticmethod
    def init_app(app):
        pass


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

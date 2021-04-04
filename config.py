import os
from werkzeug.utils import secure_filename

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ALLOWED_EXTENSION={'png', 'gif', 'jpg', 'jpeg'}
    UPLOAD_PROFILE_IMAGE = os.environ.get('UPLOAD_PROFILE_IMAGE')
    UPLOAD_PROFILE_COVER = os.environ.get('UPLOAD_COVER_IMAGE')
    MAX_CONTENT_LENGTH = 100 * 512 * 512

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

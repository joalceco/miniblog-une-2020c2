import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "DASJE#$FGQP)5644F"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir,"app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')


# class HerokuConfig(ProductionConfig):
#     @classmethod
#     def init_app(cls, app):
#         ProductionConfig.init_app(app)
#         # log to stderr
#         import logging
#         from logging import StreamHandler
#         file_handler = StreamHandler()
#         file_handler.setLevel(logging.INFO)
#         app.logger.addHandler(file_handler)


from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xf9\x82\xa6\xd1\xd1\xe8!\xbd\x1as\xc7*\xc3\x11&\xcb'
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql:///test?unix_socket=/var/run/mysqld/mysqld.sock'

DEBUG = True

#SQlALCHEMY_DATABASE_URI = 'mysql://dbname?unix_socket=/tmp/mysql/mysql.sock'
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repo')

SECRET_KEY = '\xb4\xb2\xadF\x15l\xfb\r\x059p!\xb9\xa31J+\xec\x9d\xa6j#\xf9\xc4'

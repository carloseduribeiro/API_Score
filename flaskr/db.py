__main__ = 'info'

import MySQLdb

from auth import *

try:
    conn = MySQLdb.connect(db=DB_NAME, host=DB_HOST, port=DB_PORT, user=DB_USER, passwd=DB_PASSWD)
    conn.autocommit(True)
    cursor = conn.cursor()
# except db_exceptions.OperationalError as error:
except MySQLdb.OperationalError as error:
    print("Erro: " + error.args[1])

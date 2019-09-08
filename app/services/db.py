import mysql.connector


def db_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='ope-impacta',
                                         user='root',
                                         password='1234',
                                         auth_plugin='mysql_native_password')
    return connection

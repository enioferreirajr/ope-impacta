import mysql.connector

def abrirConexao():
    connection = mysql.connector.connect(   host='localhost',
                                            database='ope-impacta',
                                            user='root',
                                            password='1234',
                                            auth_plugin='mysql_native_password')

    if connection.is_connected:
        print('MySQL está conectado!') 

    print("Validando Tabelas!")

    cursor = connection.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS Usuarios\
                                    (\
                                    IdUsuario INT AUTO_INCREMENT,\
                                    NomeUsuario varchar(60) NOT NULL UNIQUE,\
                                    Senha varchar(20) NOT NULL,\
                                    PRIMARY KEY (IdUsuario)\
                                    );'
    cursor.execute(sql)
    print('Tabela Usuarios verificada!')



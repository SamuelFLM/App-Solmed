import pyodbc


class ConexaoBancoDeDados:
    def __init__(self) -> None:
        server = "DESKTOP-TUNL46H"
        database = "CLIENTES"
        cnxn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
            + server
            + ";DATABASE="
            + database
            + ";Trusted_Connection=yes;"
        )
        self.cursor = cnxn.cursor()

    def registro(self, nome, email, celular, senha):
        validador = self.valida_usuario_existente_id(email)
        if validador:
            query = f"""INSERT INTO [dbo].[USUARIO]
            ([nome]
            ,[email]
            ,[celular]
            ,[senha])
            VALUES('{nome}', '{email}', '{celular}', '{senha}')"""
            self.cursor.execute(query)
            self.cursor.commit()
        else: print("Usuario existente")
    def obter_usuario(self):
        query = ""
        self.cursor.execute(query)
        self.cursor.commit()

    def obter_usuario_id(self):
        query = ""
        self.cursor.execute(query)
        self.cursor.commit()

    def excluir_usuario_id(self):
        query = ""
        self.cursor.execute(query)
        self.cursor.commit()

    def alterar_info_usuario_id(self):
        query = ""
        self.cursor.execute(query)
        self.cursor.commit()
    def valida_usuario_existente_id(self, email):
        query = f"SELECT EMAIL FROM USUARIO WHERE EMAIL = '{email}'"
        self.cursor.execute(query)
        dados = self.cursor.fetchval()
        if not dados:
            return True
        else: return False

if __name__ == "__main__":
    if ConexaoBancoDeDados():
        print("OK")

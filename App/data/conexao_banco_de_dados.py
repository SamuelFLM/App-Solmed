import pyodbc
import pyautogui as bot

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

    def registro(self, nome: str, email: str, celular: str, senha: str):
        validador = self.valida_usuario_existente_id(email)
        if validador:
            query = f"""INSERT INTO [dbo].[USUARIO]
            ([nome]
            ,[email]
            ,[celular]
            ,[senha])
            VALUES('{nome.strip()}', '{email.strip()}', '{celular.strip()}', '{senha.strip()}')"""
            self.cursor.execute(query)
            self.cursor.commit()
        else: bot.confirm(
                        title="ERRO",
                        text="USUARIO NAO EXISTENTE!",
                        buttons=["OK"],
                    )
        
    def obter_usuario(self):
        query = ""
        self.cursor.execute(query)
        self.cursor.commit()

    def obter_usuario_id(self, email):
        validador = self.valida_usuario_existente_id(email)
        if validador:
            query = f"SELECT EMAIL FROM USUARIO WHERE EMAIL = '{email}'"
            self.cursor.execute(query)
            self.cursor.commit()
        else:  bot.confirm(
                        title="ERRO",
                        text="USUARIO NAO EXISTENTE!",
                        buttons=["OK"],
                    )
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

    def login_sistema(self, email):
        validador_usuario = self.valida_usuario_existente_id(email)
        if not validador_usuario:
            query = f"SELECT EMAIL, SENHA, NOME FROM USUARIO WHERE EMAIL = '{email}'"
            self.cursor.execute(query)
            dados = self.cursor.fetchall()
            return dados
        else: False
        
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

from page.Register.main import MainRegister
from data.conexao_banco_de_dados import ConexaoBancoDeDados
from page.Login.main import MainLogin

class Main():
    def __init__(self) -> None:
        self.conexao = ConexaoBancoDeDados()
        self.tela_register = MainRegister(self.conexao)
        self.tela_login = MainLogin(self.conexao)
    
    def main(self):
        self.tela_register._main(self.tela_login)
        # self.tela_login._main(self.tela_register)
        
if __name__ == "__main__":
    Main().main()
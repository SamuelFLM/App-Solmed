import pyodbc

class ConexaoBancoDeDados:
    def __init__(self) -> None:
        server = 'DESKTOP-TUNL46H'
        database = 'CLIENTES'
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
        self.cursor = cnxn.cursor()

    
if __name__ == "__main__":
    if ConexaoBancoDeDados():
        print("OK")
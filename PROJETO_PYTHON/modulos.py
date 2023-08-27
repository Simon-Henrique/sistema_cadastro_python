import pyodbc

def existe_arq(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criar_arquivo(arq):
    try:
        a = open(arq, 'wt+')
    except:
        print('erro ao criar arquivo')
    else:
        print('arquivo criado')
    finally:
        a.close()

def inserir_dados(arq, tema, topico, situacao, data):
    try:
        a = open(arq, 'at')
    except:
        print()
    else:
        a.write(f'{tema}, {topico}, {situacao}, {data} \n')


def enviar_sql(tema, topico, situacao, data):
    dados_conexao = (
        "Driver={SQL Server};"
        "Server=SIMON-PC\SQLEXPRESS;"
        "Database=SIMON_ANALYTICS;"
    )

    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()
    comando = f"""insert into guia_de_estudos(tema, topico, situacao, data_inclusao) values('{tema}', '{topico}', '{situacao}', '{data}')"""
    cursor.execute(comando)
    cursor.commit()
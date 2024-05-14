import os
import re

caminho_atual = os.path.dirname(__file__)

def Main(fileName):
    code =convertCodeToString(fileName)

    code = removeComents(code)

    print(code)


def convertCodeToString(fileName):
    filePath = caminho_atual + '/' + fileName
    with open(filePath, 'r') as arquivo:
        codigo = arquivo.read()
    return codigo.replace('\n', '\\n')

def removeComents(code):
    return re.sub(r'#.*?\n', '', code, flags=re.DOTALL)

nome_arquivo = "insertion.py"
Main(nome_arquivo)

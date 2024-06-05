import os
import re

caminho_atual = os.path.dirname(__file__)

def Main(fileName):
    code =convertCodeToString(fileName)

    code = removeComents(code)

    code = splitCode(code)

    filtered_code = [item for item in code if item[1] != '']

    code = addBrackets(filtered_code)

    code = tradutor(filtered_code)

    for i in range(0, len(code)):
        print(code[i])
    for i in range(0, len(code)):
        print(code[i][1])

def convertCodeToString(fileName):
    filePath = caminho_atual + '/' + fileName
    with open(filePath, 'r') as arquivo:
        codigo = arquivo.read()
    return codigo.replace('\n', '\\n')

def removeComents(code):
    return re.sub(r'(#).*?\\n', '\n', code, flags=re.DOTALL)

def splitCode(code):
    code = repr(code)[1:-1]
    splitedCode = [[0]]
    nivel = 0
    registrador = 0
    for i in range(len(code)):
        if code[i] == '\\' and code[i + 1] == 'n':
            # print(code[i] + code[i + 1])
            splitedCode[nivel].append(code[registrador : i - 1])
            # print(code[registrador : i])
            contSpaces = 0
            verificador = True
            j = i+2
            if j < len(code)-1:
                while verificador:
                    if code[j] == " " :
                        contSpaces += 1
                        j += 1
                    else:
                        verificador = False

                splitedCode.append([contSpaces])
                nivel += 1
                i = j
                registrador = j
    
    return splitedCode

def addBrackets(code):
    brackets = 0
    nivel = code[0][0]
    for i in range(len(code)):
        if ":" in code[i][1] and not "print" in code[i][1]:
            code[i][1] = code[i][1].replace(":", "{")
            brackets += 1

        if nivel > code[i][0] and brackets > 0:
            numBrackets = int((nivel - code[i][0])/4)
            print(numBrackets)
            code[i][1] = code[i][0] * " " + "}" * numBrackets + "\n" + code[i][0] * " " + code[i][1]
            brackets -= 1
        else:
            code[i][1] = code[i][0] * " " + code[i][1]
        
        nivel = code[i][0]
        
    return code

def tradutor(code):
    for i in range(len(code)):
        if "def"in code[i][1]:
            code[i][1] = code[i][1].replace("def", "function")
    return code

nome_arquivo = "insertion.py"

Main(nome_arquivo)

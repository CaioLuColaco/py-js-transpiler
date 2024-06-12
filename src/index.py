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

    # for i in range(0, len(code)):
    #     print(code[i])
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
            splitedCode[nivel].append(code[registrador : i - 1])
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
            code[i][1] = code[i][0] * " " + "}\n" * numBrackets + code[i][0] * " " + code[i][1]
            brackets -= 1
        else:
            code[i][1] = code[i][0] * " " + code[i][1]
        
        nivel = code[i][0]
        
    return code

def tradutor(code):
    for i in range(len(code)):
        if "def"in code[i][1]:
            code[i][1] = code[i][1].replace("def", "function")

        if "print" in code[i][1]:
            code[i][1] = code[i][1].replace("print", "console.log")

        words = code[i][1].split()
        if len(words) > 1 and "=" in words:
            var_index = words.index("=") - 1
            if var_index >= 0 and words[var_index] not in ["if", "for", "while"]:
                last_char = words[var_index][len(words[var_index]) - 1 :len(words[var_index])]
                if last_char == ']':
                    code[i][1] = code[i][1].replace(words[var_index],f"{words[var_index]}")
                else:    
                    code[i][1] = code[i][1].replace(words[var_index], f"let {words[var_index]}", 1)

        if words[0] == "while" or "while" in code[i][1]:
            position_while = code[i][1].find("while")
            condition_start = position_while + len("while")
            condition = code[i][1][condition_start:].strip()
            code[i][1] = code[i][1][:position_while] + f"while ({condition})"
            code[i][1] = code[i][1].replace("{", "") + "{"
            code[i][1] = code[i][1].replace("and", "&&").replace("or", "||")
        
        if words[0] == "for" or "for" in code[i][1]:
            position_for = code[i][1].find("for")
            for_index = words.index("for")
            var_name = words[for_index + 1]
            in_keyword_index = code[i][1].find("in")
            iter_expression = code[i][1][in_keyword_index + 2:].strip()
            if iter_expression.startswith("range("):
                range_args = iter_expression[6:-2].split(',')
                if len(range_args) == 1:
                    start = 0
                    end = range_args[0]
                    step = 1
                elif len(range_args) == 2:
                    start = range_args[0]
                    end = range_args[1]
                    step = 1
                elif len(range_args) == 3:
                    start = range_args[0]
                    end = range_args[1]
                    step = range_args[2]
                # code[i][1] = " " * code[i][0] + f"for (let {var_name} = {start}; {var_name} < {end}; {var_name} += {step})"
                code[i][1] = code[i][1][:position_for] + f"for (let {var_name} = {start}; {var_name} < {end}; {var_name} += {step})"
                code[i][1] = code[i][1].replace("{", "") + "{"
            else:
                code[i][1] = " " * code[i][0] + f"for (let {var_name} of {iter_expression})"
                code[i][1] = code[i][1].replace("{", "") + "{"

            code[i][1] = re.sub(r'len\((.*?)\)', r'\1.length', code[i][1])

        if words[0] == "if":
            condition_start = code[i][1].find("if") + len("if")
            condition = code[i][1][condition_start:].strip()
            code[i][1] = " " * code[i][0] + f"if ({condition})"
            code[i][1] = code[i][1].replace("{", "") + "{"
            code[i][1] = code[i][1].replace("and", "&&").replace("or", "||")

        code[i][1] = re.sub(r'len\((.*?)\)', r'\1.length', code[i][1])

    return code

nome_arquivo = "bubbleSort.py"

Main(nome_arquivo)
